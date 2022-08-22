from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import CreateView, ListView, UpdateView
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *

# Create your views here.
class SignUpView(CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

class UserProfileView(ListView):
    model = CustomUser
    template_name = 'profile.html'


class ProfileUpdateView(UpdateView):

    form_class = CustomUserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'registration/profile_edit.html'

    def get_object(self):
        return self.request.user