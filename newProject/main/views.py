from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def clinics(request):
    return render(request, 'main/clinics.html')

def kalugak1k2(request):
    return render(request, 'main/kalugak1k2.html')

def kalugak3k4(request):
    return render(request, 'main/kalugak3k4.html')

def sergievsk(request):
    return render(request, 'main/sergievsk.html')