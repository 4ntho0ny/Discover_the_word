from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"), # Starting Page
    path("play", views.play_page, name="play_page"), # Game Page
    path("winner", views.result_page, name="winner_page") # Result Page
]
