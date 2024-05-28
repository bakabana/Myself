"""
URL configuration for MSY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pack_info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('creer_compte/', views.creer_compte, name='creer_compte'),
    path('', views.index, name='index'),
    path('equipement/list/', views.equipement_list, name='equipement_list'),
    path('equipement/create/', views.createEquipement, name='create_equipement'),
    path('equipement/<int:pk>/update/', views.updateEquipement, name='update_equipement'),
    path('equipement/<int:pk>/delete/', views.deleteEquipement, name='delete_equipement'),


    path('software/list/', views.software_list, name='software_list'),
    path('create/software/', views.createSoftware, name='create_software'),
    path('software/<int:pk>/update/', views.updateSoftware, name='update_software'),
    path('software/<int:pk>/delete/', views.deleteSoftware, name='delete_software'),


    path('capacite/list/', views.capacite_list, name='capacite_list'),
    path('capacite/create/', views.createCapacite, name='create_capacite'),
    path('capacite/<int:pk>/update/', views.updateCapacite, name='update_capacite'),
    path('capacite/<int:pk>/delete/', views.deleteCapacite, name='delete_capacite'),





]
