from django.contrib.auth.forms import forms
from django.forms import ModelForm
from .models import Song

class AudioForm(ModelForm):
    class Meta:
        model = Song
        fields = ['songs']
