import django.views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.http.request import HttpRequest
from . import models, forms


class Home(View):
    def get(self, request):
        return render(request=request, template_name="hub/home.html")


class DashBoard(LoginRequiredMixin, View):

    def get(self, request):
        return render(request=request, template_name="hub/Dashboard.html")


class About(View):
    def get(self, request: HttpRequest):
        context = {}
        if request.user.is_authenticated:
            context['base'] = 'RSFS/LoginBase.html'
        else:
            context['base'] = 'RSFS/NonLoginBase.html'
        return render(request=request, template_name='hub/About.html', context=context)


class ShipperDashboard(LoginRequiredMixin, View):

    def get(self, request: HttpRequest):
        return render(request=request, template_name='hub/ShipperDashboard.html')


class ShipperListShipments(LoginRequiredMixin, ListView):
    model = models.Shipper
    context_object_name = 'shipmentList'
    paginate_by = 25
    template_name = "hub/ShipperListShipment.html"

    def get_queryset(self):
        return self.model.manager.all().filter(self.request.user.pk)


class LogisticsDashboard(LoginRequiredMixin, View):

    def get(self, request: HttpRequest):
        return render(request=request, template_name='hub/LogisticsDashboard.html')


class NewShipment(CreateView):
    model = models.Shipment
    form_class = forms.ShipmentForm
    template_name = "hub/NewShipment.html"
    success_url = reverse_lazy('hub:Dashboard')

    def form_valid(self, form):
        form.save(commit=True)
        return redirect(to=self.success_url)
