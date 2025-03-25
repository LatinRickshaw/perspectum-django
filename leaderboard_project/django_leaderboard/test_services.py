import json
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import User, Submission
from .services import DataLoader, LeaderboardService
from datetime import date

class DataLoaderTest(TestCase):

    def setUp(self):
        self.test_data = [
            {
                "name": "testuser1",
                "submissions": [
                    {"name": "submission1", "date": "2025-03-25", "score": 100},
                    {"name": "submission2", "date": "2025-03-25", "score": 200}
                ]
            },
            {
                "name": "testuser2",
                "submissions": [
                    {"name": "submission3", "date": "2025-03-25", "score": 300}
                ]
            }
        ]
        self.test_file = SimpleUploadedFile("scores.json", json.dumps(self.test_data).encode())

    def test_load_data(self):
        DataLoader.load_data(self.test_file)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Submission.objects.count(), 3)
        self.assertEqual(User.objects.get(name="testuser1").submissions.count(), 2)
        self.assertEqual(User.objects.get(name="testuser2").submissions.count(), 1)

class LeaderboardServiceTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create(name="testuser1")
        self.user2 = User.objects.create(name="testuser2")
        self.user3 = User.objects.create(name="testuser3")

        Submission.objects.create(user=self.user1, name="submission1", date=date.today(), score=100)
        Submission.objects.create(user=self.user1, name="submission2", date=date.today(), score=200)
        Submission.objects.create(user=self.user1, name="submission3", date=date.today(), score=300)

        Submission.objects.create(user=self.user2, name="submission4", date=date.today(), score=400)
        Submission.objects.create(user=self.user2, name="submission5", date=date.today(), score=500)
        Submission.objects.create(user=self.user2, name="submission6", date=date.today(), score=600)

        Submission.objects.create(user=self.user3, name="submission7", date=date.today(), score=700)
        Submission.objects.create(user=self.user3, name="submission8", date=date.today(), score=800)

    def test_get_leaderboard(self):
        leaderboard = LeaderboardService.get_leaderboard()
        self.assertEqual(len(leaderboard), 2)
        self.assertEqual(leaderboard[0][0], "testuser2")
        self.assertEqual(leaderboard[1][0], "testuser1")
        self.assertEqual(leaderboard[0][1], 1500)
        self.assertEqual(leaderboard[1][1], 600)