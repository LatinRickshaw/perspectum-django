import json
from .models import User, Submission
from django.db.models import Sum

class DataLoader:
    @staticmethod
    def load_data(file_path='scores.json'):
        with open(file_path) as file:
            data = json.load(file)
        for entry in data:
            user, created = User.objects.get_or_create(name=entry['name'])
            for submission in entry['submissions']:
                Submission.objects.create(
                    user=user,
                    name=submission['name'],
                    date=submission['date'],
                    score=submission['score']
                )


class LeaderboardService:
    @staticmethod
    def get_leaderboard():
        users = User.objects.annotate(total_score=Sum('submissions__score'))
        filtered_users = []
        
        for user in users:
            submissions = list(user.submissions.all())
            if len(submissions) < 3:
                continue
            
            top_submissions = sorted(submissions, key=lambda x: x.score, reverse=True)[:24]
            total_score = sum(s.score for s in top_submissions)
            filtered_users.append((user.name, total_score))
        
        return sorted(filtered_users, key=lambda x: x[1], reverse=True)
