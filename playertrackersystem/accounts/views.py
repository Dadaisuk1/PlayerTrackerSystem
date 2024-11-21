from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            player = Player.objects.get(username=username)
            if check_password(password, player.password):  # Verify hashed password
                request.session['player_id'] = player.playerID  # Custom session management
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')
        except Player.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


# Logout view
def logout_view(request):
    if 'player_id' in request.session:
        del request.session['player_id']  # Remove the player ID from session
    return redirect('login')


# Home view (protected by login_required)

def home(request):
    player_id = request.session.get('player_id')
    if player_id:
        player = Player.objects.get(playerID=player_id)
        return render(request, 'home.html', {'player': player})
    return redirect('login')


# Register a new player
def register_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()  # Password will be hashed automatically
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'register.html', {'form': form})


# View all players (protected by login_required)

def player_list(request):
    players = Player.objects.all()  # Get all players
    return render(request, 'player_list.html', {'players': players})


# Update an existing player

def update_player(request, playerID):
    player = get_object_or_404(Player, playerID=playerID)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'update_player.html', {'form': form})


# Delete a player

def delete_player(request, playerID):
    player = get_object_or_404(Player, playerID=playerID)
    if request.method == 'POST':
        player.delete()  # Delete the player
        return redirect('player_list')
    return render(request, 'delete_player.html', {'player': player})
