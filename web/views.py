from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def open_water(request):
    return render(request, "open_water.html")

def tours(request):
    return render(request, "tours.html")

def primera_vez(request):
    return render(request, "primera_vez.html")

def tours_local(request):
    return render(request, "tours_local.html")

def tours_tortuga(request):
    return render(request, "tours_tortuga.html")

def refrescamiento(request):
    return render(request, "refrescamiento.html")