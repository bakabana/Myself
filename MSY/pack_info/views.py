from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from .models import Equipement, Software, Capacite
from .forms import EquipementForm, SoftwareForm, CapaciteForm ,ConnexionForm,SearchForm,SearchsForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Utilisateur
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Définition d'une classe utilisateur pour stocker les informations des utilisateur

# Fonction pour créer un nouveau compte


def index(request):
    return render(request, 'pack_info/index.html')

# Views for Equipement CRUD operations

def createEquipement(request):
    if request.method == 'POST':
        form = EquipementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipement_list')  # Rediriger vers la liste des équipements
    else:
        form = EquipementForm()
    return render(request, 'pack_info/create_equipement.html', {'form': form})

def equipement_list(request):
    form = SearchForm()
    query = request.GET.get('query')
    if query:
        equipements = Equipement.objects.filter(NomEquipement__icontains=query).order_by('NomEquipement')
    else:
        equipements = Equipement.objects.all().order_by('NomEquipement')
    return render(request, 'pack_info/affiche_equipement.html', {'equipements': equipements, 'form': form})


def updateEquipement(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    if request.method == 'POST':
        form = EquipementForm(request.POST, instance=equipement)
        if form.is_valid():
            form.save()
            return redirect('equipement_list')
    else:
        form = EquipementForm(instance=equipement)
    return render(request, 'pack_info/update_equipement.html', {'form': form})

def deleteEquipement(request, pk):
    equipement = get_object_or_404(Equipement, pk=pk)
    if request.method == 'POST':
        equipement.delete()
        return redirect('equipement_list')
    return render(request, 'pack_info/delete_equipement.html', {'equipement': equipement})

# Views for Software CRUD operations (similar to Equipement CRUD)
def software_list(request):
    form = SearchsForm(request.GET or None)
    query = request.GET.get('query')
    order_by = request.GET.get('order_by', 'Logiciel')  # Default sort by Logiciel
    softwares = Software.objects.all()

    if query:
        softwares = softwares.filter(Logiciel__icontains=query)  # Assurez-vous de filtrer par le bon champ
    
    softwares = softwares.order_by(order_by)

    return render(request, 'pack_info/affich_software.html', {
        'softwares': softwares,
        'form': form,
        'order_by': order_by
    })

def createSoftware(request):
    if request.method == 'POST':
        form = SoftwareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('software_list')  # Rediriger vers la liste des logiciels
    else:
        form = SoftwareForm()  # Assurez-vous d'utiliser SoftwareForm
    return render(request, 'pack_info/create_software.html', {'form': form})


def updateSoftware(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        form = SoftwareForm(request.POST, instance=software)
        if form.is_valid():
            form.save()
            return redirect('software_list')
    else:
        form = EquipementForm(instance=software)
    return render(request, 'pack_info/update_software.html', {'form': form})

def deleteSoftware(request, pk):
    software = get_object_or_404(Software, pk=pk)
    if request.method == 'POST':
        software.delete()
        return redirect('software_list')
    return render(request, 'pack_info/delete_software.html', {'software': software})


# Views for Capacite CRUD operations (similar to Equipement CRUD)

#def capacite_list(request):
    #capacites = Capacite.objects.all()
    #return render(request, 'pack_info/affiche_capacite.html', {'capacites': capacites})

def capacite_list(request):
    form = SearchForm()
    query = request.GET.get('query')
    if query:
        capacites = Capacite.objects.filter(NomEquipement__icontains=query).order_by('NomEquipement')
    else:
        capacites = Capacite.objects.all().order_by('NomEquipement')
    return render(request, 'pack_info/affiche_capacite.html', {'capacites': capacites, 'form': form})


def createCapacite(request):
    if request.method == 'POST':
        form = CapaciteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('capacite_list')  # Rediriger vers la liste des équipements
    else:
        form = EquipementForm()
    return render(request, 'pack_info/create_capacite.html', {'form': form})



def updateCapacite(request, pk):
    capacite = get_object_or_404(Capacite, pk=pk)
    if request.method == 'POST':
        form = CapaciteForm(request.POST, instance=capacite)
        if form.is_valid():
            form.save()
            return redirect('capacite_list')
    else:
        form = EquipementForm(instance=capacite)
    return render(request, 'pack_info/update_capacite.html', {'form': form})

def deleteCapacite(request, pk):
    software = get_object_or_404(Capacite, pk=pk)
    if request.method == 'POST':
        software.delete()
        return redirect('capacite_list')
    return render(request, 'pack_info/delete_software.html', {'capacite': Capacite})
