
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toners.urls')),
    path('laptops/', include('laptop.urls'), name='laptops'),
    path('accounts/', include('allauth.urls')),
    path('assets/', include('assets.urls'), name='assets'),
    path('asset_trans/', include('asset_trans.urls'), name='asset_trans'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
