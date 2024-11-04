from django.shortcuts import render

def index(request):
    return render(request,"core/index.html")

def clasicos(request):
    return render(request,"core/clasicos.html")

def actuales(request):
    return render(request,"core/actuales.html")

def galeria(request):
    return render(request,"core/galeria.html")