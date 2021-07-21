from django.urls import path
from chess_players.views import *

urlpatterns = [
    path('', chess_players, name='chess_players'),
]