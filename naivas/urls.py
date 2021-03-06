
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.toners.urls')),
    path('accounts/', include('allauth.urls')),
    path('assets/', include('apps.assets.urls'), name='assets'),
    path('repairs/', include('apps.repair.urls'), name='repairs'),
    path('asset_trans/', include('apps.asset_trans.urls'), name='asset_trans'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
