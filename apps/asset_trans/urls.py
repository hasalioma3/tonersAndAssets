from django.urls import path
from .views import index

app_name = 'assets_trans'

urlpatterns = [
    path('',index,name='home')
]
