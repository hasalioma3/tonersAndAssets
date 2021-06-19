from django.contrib import admin
from .models import Branch, Tonermodels, Toners


class TonersAdmin(admin.ModelAdmin):
    list_display = ('branch','tonermodels', 'reading','created_on','created_by')  
    search_fields =('branch__name',)



admin.site.register(Branch)
admin.site.register(Tonermodels)
admin.site.register(Toners, TonersAdmin) 