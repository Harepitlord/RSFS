import django.views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.views import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from . import models,forms


class Home(View):
    def get(self, request:WSGIRequest):
        return render(request=request, template_name="hub/home.html")


class DashBoard(LoginRequiredMixin, View):
    login_url = reverse_lazy('UserManagement:Login')

    def get(self, request:WSGIRequest):
        return render(request=request, template_name="hub/Dashboard.html")


class About(View):
    def get(self, request:WSGIRequest):
        context = {}
        if request.user.is_authenticated:
            context['base'] = 'RSFS/LoginBase.html'
        else:
            context['base'] = 'RSFS/NonLoginBase.html'
        return render(request=request, template_name='hub/About.html',context=context)


class NewShipment(CreateView):
    model = models.Shipment
    form_class = forms.ShipmentForm
    template_name = "hub/NewShipment.html"
    success_url = reverse_lazy('hub:Dashboard')

    def form_valid(self, form):
        form.save(commit=True)
        return redirect(to=self.success_url)