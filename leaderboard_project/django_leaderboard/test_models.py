from django.test import TestCase
from .models import User, Submission
from datetime import date

class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(name="testuser")

    def test_user_creation(self):
        self.assertEqual(self.user.name, "testuser")
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(str(self.user), self.user.name)

class SubmissionModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(name="testuser")
        self.submission = Submission.objects.create(
            user=self.user,
            name="testsubmission",
            date=date.today(),
            score=100
        )

    def test_submission_creation(self):
        self.assertEqual(self.submission.name, "testsubmission")
        self.assertEqual(self.submission.user.name, "testuser")
        self.assertEqual(self.submission.score, 100)
        self.assertTrue(isinstance(self.submission, Submission))
        self.assertEqual(str(self.submission), self.submission.name)