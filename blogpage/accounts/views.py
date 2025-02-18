from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from main.forms import ContactUsForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login") #redirect to login upon successful registration
    template_name = "registration/signup.html"
