from django.shortcuts import render

def home(request):
    return render(request, 'institucional/home.html')

def quem_somos(request):
    return render(request, 'institucional/quem_somos.html')