from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render


class Home(View):
    def get(self, request):
        return render(request=request, template_name="hub/home.html")


class DashBoard(LoginRequiredMixin, View):
    login_url = reverse_lazy('UserManagement:Login')

    def get(self, request):
        return render(request=request, template_name="hub/Dashboard.html")


class About(View):
    def get(self, request):
        return render(request=request, template_name='hub/About.html')
