from django.shortcuts import render
from .models import Hero, Game
from .forms import GameForm, HeroForm

# Create your views here.
def home_page(request):
    games = Game.objects.all()
    return render(request, 'home.html', {'games': games})

def index(request):
    games = Game.objects.all()
    return render(request, 'index.html', {'games': games})