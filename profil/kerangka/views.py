import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)

def home(request):
    logger.info("Home view is being accessed")
    return render(request, 'kerangka/home.html')

def profil_umum(request):
    return render(request, 'kerangka/profil_umum.html')

def pendidikan(request):
    return render(request, 'kerangka/pendidikan.html')

def pengalaman_kerja(request):
    return render(request, 'kerangka/pengalaman_kerja.html')

def sosial_media(request):
    return render(request, 'kerangka/sosial_media.html')
