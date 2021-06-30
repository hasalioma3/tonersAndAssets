from django.contrib import admin

from .models import  Location,Staff,Category,Asset,Delivery,DeliveryAsset, Logo

# admin.site.register(Make)
# admin.site.register(Amodel)
admin.site.register(Location)
admin.site.register(Staff)
admin.site.register(Category)
admin.site.register(Asset)
admin.site.register(Delivery)
admin.site.register(DeliveryAsset)
admin.site.register(Logo)

