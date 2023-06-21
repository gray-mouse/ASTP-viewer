from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clinics', views.clinics, name='clinics'),
    path('kalugak1k2', views.kalugak1k2, name='kalugak1k2'),
    path('kalugak3k4', views.kalugak3k4, name='kalugak3k4'),
    path('sergievsk', views.sergievsk, name='sergievsk')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #подключение всех статических файлов