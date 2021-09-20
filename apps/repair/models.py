from django.db import models
from apps.assets.models import Asset, Staff,Location,Delivery
# Create your models here.
# Vendor


class Vendor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name
# delivery


class RepairDelivery(models.Model):
    delivery = models.OneToOneField(Delivery, on_delete=models.CASCADE, null=True, blank=True)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, null=True, blank=True, related_name="vendor")

    def __str__(self):
        return str(self.delivery.deliveryNo) + ' ' + str(self.vendor.name)

    # @property
    # def key1(self):
    #     return str(self.id).zfill(6)

    # @property
    # def get_delivery_items_no(self):
    #     deliveryassets = self.deliveryasset_set.all()
    #     total = sum([asset.quantity for asset in deliveryassets])
    #     return total

    # def get_delivery_assets(self):
    #     deliveryassets = self.deliveryasset_set.all()
    #     return deliveryassets


class RepairTrans(models.Model):
    asset = models.ForeignKey(
        Asset, on_delete=models.CASCADE, null=True, blank=True,)
    repair_delivery = models.ForeignKey(
        RepairDelivery, on_delete=models.CASCADE, null=True, blank=True)
    date_dispatched = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default=False)

    def __str__(self):
        return str(self.repair_delivery.vendor)
