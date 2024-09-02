from django.shortcuts import render, get_object_or_404

from .models import UsersGame

# Create your views here.
from django.http import HttpResponse


def index(request):
    games = UsersGame.objects.all()
    context = {
        "games": games,
    }
    return render(request, "games/index.html", context)

def game(request, game_id):
    user_game = get_object_or_404(UsersGame, pk=game_id)
    return render(request, "games/game.html", {"game": user_game})

def score(request, game_id):
    return HttpResponse("You're looking at score of game %s." % game_id)