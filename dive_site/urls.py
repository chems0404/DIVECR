from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Tours
    path('tours/', views.tours, name='tours'),
    path('tours/local/', views.tours_local, name='tours_local'),
    path('tours/isla-tortuga/', views.tours_tortuga, name='tours_tortuga'),

    # Cursos base
    path('cursos/open-water/', views.open_water, name='open_water'),
    path('cursos/refrescamiento/', views.refrescamiento, name='refrescamiento'),
    path('primera-vez/', views.primera_vez, name='primera_vez'),

    # Educación continua
    path('cursos/advanced-adventure/', views.advanced_adventure, name='advanced_adventure'),
    path('cursos/react-right-rcp/', views.react_right_rcp, name='react_right_rcp'),
    path('cursos/diver-stress-rescue/', views.diver_stress_rescue, name='diver_stress_rescue'),

    # Especialidades
    path('especialidades/nitrox/', views.nitrox, name='nitrox'),
    path('especialidades/profundo/', views.profundo, name='profundo'),
    path('especialidades/flotabilidad/', views.flotabilidad, name='flotabilidad'),
    path('especialidades/nocturno/', views.nocturno, name='nocturno'),

    # Comunidad / Proyectos (Apasionados por el océano)
    path('oceano/apasionados/', views.apasionados_oceano, name='apasionados_oceano'),

    path('conocenos/', views.conocenos, name='conocenos'),
    path('testimonios/', views.testimonios, name='testimonios'),
    path('galeria/', views.galeria, name='galeria'),



]
