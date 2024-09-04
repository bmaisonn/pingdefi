from django.urls import path

from . import views

app_name="games"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:game_id>", views.game, name="game"),
    path("<int:game_id>/score", views.score, name="score")
]