from django.urls import path
from .views import LeaderboardView

urlpatterns = [
    path('leaderboard/', LeaderboardView.leaderboard, name='leaderboard'),
]
