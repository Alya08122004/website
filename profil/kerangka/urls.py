from django.contrib import admin
from django.urls import path
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  
    path('profil_umum/', views.profil_umum, name='profil_umum'),
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('pengalaman/', views.pengalaman_kerja, name='pengalaman_kerja'),
    path('sosial-media/', views.sosial_media, name='sosial_media'),
]
