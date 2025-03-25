from django.shortcuts import render
from .services import LeaderboardService

class LeaderboardView:
    @staticmethod
    def leaderboard(request):
        ranked_users = LeaderboardService.get_leaderboard()
        return render(request, 'leaderboard.html', {'leaderboard': ranked_users})
    

