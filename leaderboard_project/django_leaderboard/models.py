from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submissions')
    name = models.CharField(max_length=255)
    date = models.DateField()
    score = models.IntegerField()
    
