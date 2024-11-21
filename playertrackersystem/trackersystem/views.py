from django.shortcuts import render
from .models import Hero, Game
from .forms import GameForm, HeroForm

# Create your views here.
def home_page(Httprequest):
    games = Game.objects.all()
    return render(Httprequest, 'home.html', {'games': games})