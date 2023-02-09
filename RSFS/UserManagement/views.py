from django.contrib.auth import get_user_model
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import PasswordChangeView, LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View

from . import forms
from . import models

backend = 'UserManagement.backend.EmailBackend'

class Signup(CreateView):
    model = get_user_model()
    form_class = forms.NewUser
    template_name = 'UserManagement/Signup.html'
    success_url = reverse_lazy("hub:Dashboard")

    def form_valid(self, form):
        form.save(commit=True)
        user = authenticate(username=form.cleaned_data['email'],password=form.cleaned_data['password'])
        login(request=self.request,user=user)
        return redirect(to=self.success_url)


class Login(LoginView):
    template_name = 'UserManagement/Login.html'

class Logout(LogoutView):
    next_page = reverse_lazy("hub:Home")



