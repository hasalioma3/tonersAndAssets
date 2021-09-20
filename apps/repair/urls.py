from django.urls import path
from .views import index

app_name='repairs'

urlpatterns = [
    path('',index, name='home' ),
]