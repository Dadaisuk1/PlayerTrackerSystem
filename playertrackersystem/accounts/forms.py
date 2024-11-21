from django import forms
from .models import Player
from django.contrib.auth.hashers import make_password

class PlayerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Player
        fields = ['username', 'password']

    def save(self, commit=True):
        player = super().save(commit=False)
        player.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            player.save()
        return player
