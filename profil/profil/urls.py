from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kerangka.urls')),  # Mengarahkan root URL ke urls.py di aplikasi kerangka
]
