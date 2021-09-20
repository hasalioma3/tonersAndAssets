from django.contrib import admin

from .models import Vendor,Location,Staff,Asset,Delivery,DeliveryAsset, Logo

admin.site.register(Location)
admin.site.register(Vendor)
admin.site.register(Staff)
admin.site.register(Asset)
admin.site.register(Delivery)
admin.site.register(DeliveryAsset)
admin.site.register(Logo)

