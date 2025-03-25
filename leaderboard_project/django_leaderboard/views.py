import os
from django.shortcuts import render
from .services import LeaderboardService

def leaderboard_view(request):
    min_submissions = int(os.getenv('MIN_SUBMISSIONS', 3))
    max_submissions = int(os.getenv('MAX_SUBMISSIONS', 24))
    
    leaderboard = LeaderboardService.get_leaderboard(min_submissions=min_submissions, max_submissions=max_submissions)
    
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})
