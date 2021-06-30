from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Make(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True,)

#     def __str__(self):
#         return self.name


# class Amodel(models.Model):
#     name = models.CharField(max_length=200, null=True, blank=True)
#     make = models.ForeignKey(Make, related_name='Model',
#                              null=True, blank=True, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


class Location(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Staff(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(
        'Location', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.user)


class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Logo(models.Model):
    logo = models.ImageField(upload_to="static/img/logo")


class Asset(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    barcode = models.CharField(max_length=200, null=True, blank=True,)
    serialNumber = models.CharField(max_length=200, null=True, blank=True)
    accessory = models.BooleanField(default=False)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True)
    transit = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, blank=True, null=True)
    date_dispatched = models.DateTimeField(auto_now_add=True)
    dispatched = models.BooleanField(default=False)
    deliveryNo = models.CharField(max_length=200, null=True, blank=True)
    fromLocation = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    # toLocation = models.ForeignKey(
    #     Location, on_delete=models.CASCADE, null=True, blank=True, related_name="toLocation")
    toLocation = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.deliveryNo

    @property
    def key1(self):
        return str(self.id).zfill(6)

    @property
    def get_delivery_items_no(self):
        deliveryassets = self.deliveryasset_set.all()
        total = sum([asset.quantity for asset in deliveryassets])
        return total

    def get_delivery_assets(self):
        deliveryassets = self.deliveryasset_set.all()
        return deliveryassets


class DeliveryAsset(models.Model):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, null=True, blank=True)
    delivery = models.ForeignKey(
        Delivery, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_dispatched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.asset)

    def get_deliveryNoteNo(self):
        dnn = self.delivery_set.all()
        return dnn
