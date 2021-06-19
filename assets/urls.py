from django.urls import path
from . import views

app_name='assets'
urlpatterns=[
    path('',views.assets, name='index'),
    path('update_assets/',views.updateAsset, name='update_assets'),
    path('process_Response/',views.processResponse, name='process_Response'),
    path('pdf/<pk>',views.deliveries_pdf, name='pdf'),
 
]