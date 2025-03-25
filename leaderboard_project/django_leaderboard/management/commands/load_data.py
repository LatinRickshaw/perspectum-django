import json
from django.core.management.base import BaseCommand
from django_leaderboard.models import User, Submission
from django.utils.dateparse import parse_date
import datetime

class Command(BaseCommand):
    help = 'Load sample leaderboard data from scores.json'

    def handle(self, *args, **options):
        try:
            with open('django_leaderboard/data/scores.json', 'r') as file:
                data = json.load(file)

            for entry in data:
                user, created = User.objects.get_or_create(name=entry['name'])
                for submission in entry['submissions']:
                    # Ensure date format is correct
                    date_str = submission.get('date', None)
                    parsed_date = None
                    
                    if date_str:
                        try:
                            # Convert dd/mm/YY to YYYY-MM-DD
                            parsed_date = datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
                        except ValueError:
                            self.stderr.write(self.style.WARNING(
                                f"Invalid date '{date_str}' for submission '{submission['name']}', setting default date."
                            ))
                            parsed_date = datetime.date.today()

                    Submission.objects.create(
                        user=user,
                        name=submission['name'],
                        date=parsed_date,  # Ensure a valid date is always used
                        score=submission['score']
                    )
            
            self.stdout.write(self.style.SUCCESS('Successfully loaded data into the database.'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error loading data: {e}'))
