from django.contrib import admin
from .models import Laptop, Laptopmodel, Department


class LaptopsAdmin(admin.ModelAdmin):
    list_display = ('department','laptopmodel', 'user','barcode','created_on')  
    search_fields =('user__name',)



admin.site.register(Laptop, LaptopsAdmin)
admin.site.register(Laptopmodel)
admin.site.register(Department) 