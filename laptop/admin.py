from django.contrib import admin
from .models import Laptop_trans,Department


class LaptopsAdmin(admin.ModelAdmin):
    list_display = ('department', 'user', 'laptop' )
    search_fields =('user__name',)


admin.site.register(Laptop_trans, LaptopsAdmin)
admin.site.register(Department) 
