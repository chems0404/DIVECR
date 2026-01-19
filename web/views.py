from django.shortcuts import render


# ================= HOME =================
def home(request):
    return render(request, "home.html")


# ================= TOURS =================
def tours(request):
    return render(request, "tours.html")


def tours_local(request):
    return render(request, "tours_local.html")


def tours_tortuga(request):
    return render(request, "tours_tortuga.html")


# ================= CURSOS BASE =================
def open_water(request):
    return render(request, "open_water.html")


def refrescamiento(request):
    return render(request, "refrescamiento.html")


def primera_vez(request):
    return render(request, "primera_vez.html")


# ================= EDUCACIÓN CONTINUA =================
def advanced_adventure(request):
    return render(request, "advanced_adventure.html")


def react_right_rcp(request):
    return render(request, "react_right_rcp.html")


def diver_stress_rescue(request):
    return render(request, "diver_stress_rescue.html")


# ================= ESPECIALIDADES =================
def nitrox(request):
    return render(request, "nitrox.html")


def profundo(request):
    return render(request, "profundo.html")


def flotabilidad(request):
    return render(request, "flotabilidad.html")


def nocturno(request):
    return render(request, "nocturno.html")


# ================= COMUNIDAD / OCÉANO =================
def apasionados_oceano(request):
    """
    Página placeholder.
    Más adelante aquí irá el template de proyectos / conservación.
    """
    return render(request, "apasionados_oceano.html")
