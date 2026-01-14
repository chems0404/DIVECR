from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('tours/', views.tours, name='tours'),
    path('cursos/open-water/', views.open_water, name='open_water'),
    path('primera-vez/', views.primera_vez, name='primera_vez'),
    path("tours/local/", views.tours_local, name="tours_local"),
    path("tours/isla-tortuga/", views.tours_tortuga, name="tours_tortuga"),
    path("cursos/refrescamiento/", views.refrescamiento, name="refrescamiento"),

]

