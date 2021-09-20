from django.contrib import admin


from .models import RepairDelivery, RepairTrans, Vendor

admin.site.empty_value_display = '(None)'


@admin.register(RepairDelivery)
class RepairDeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery', 'vendor', )
    search_fields = ('vendor', 'delivery__fromLocation',
                     'delivery__deliveryNo')


@admin.register(RepairTrans)
class RepairTransAdmin(admin.ModelAdmin):
    list_display = ('asset', 'repair_delivery', 'date_dispatched', 'received', )
    search_fields = (
        'asset__name', 
        'asset__barcode',
        'asset__serialNumber', 
        'repair_delivery__delivery__deliveryNo',
         )


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', )
    search_fields = ('name',)
