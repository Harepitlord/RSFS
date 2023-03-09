from django import forms
from . import models

cargoTypeChoices = ('Inflammable', 'Fragile', 'Perishable', 'Non-Perishable', 'Livestock', 'Cautious')


class CargoForm(forms.ModelForm):
    cargoType = forms.ChoiceField(choices=cargoTypeChoices)
    cargoType.widget = forms.Select(attrs={'class': 'signRadio'})


class ShipmentForm(forms.ModelForm):
    class Meta:
        model = models.Shipment
        fields = ("Shipper_Name", "Shipment_Company", "Receiver_Name", "Source", "Destination")
