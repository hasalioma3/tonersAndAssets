from django.urls import path
from . import views

app_name='assets'
urlpatterns=[
    path('',views.assets, name='index'),
    path('update_assets/',views.updateAsset, name='update_assets'),
    path('deliveries/',views.deliveries, name='deliveries'),
    path('process_Response/',views.processResponse, name='process_Response'),
    path('pdfs/<pk>', views.renderPDF, name='pdfs'),
 
]
