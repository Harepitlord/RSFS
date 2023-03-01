from django.db import models


# Create your models here.
class Shipment(models.Model):
    shipmentId = models.CharField(name="shipmentId",max_length=20)
    ShipperName = models.CharField(name="Shipper_Name",max_length=40)
    ShipmentCompany = models.CharField(name="Shipment_Company",max_length=40)
    ReceiverName = models.CharField(name="Receiver_Name",max_length=30)
    source = models.CharField(name="Source",max_length=25)
    destination = models.CharField(name="Destination",max_length=25)
    cargoDoc = models.FileField(name="Cargo_Doc")


class CargoDetails(models.Model):
    cargoName = models.CharField(name="Cargo_Name",max_length=35)
    cargoType = models.CharField(name="Cargo_Type",max_length=15)

    shipmentId = models.ForeignKey(to=Shipment,on_delete=models.CASCADE)
