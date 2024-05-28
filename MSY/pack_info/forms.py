from django import forms
from .models import Equipement, Software, Capacite, Utilisateur

class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class CreationCompteForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class EquipementForm(forms.ModelForm):
    class Meta:
        model = Equipement
        fields = ['NatureEquipement', 'NomEquipement', 'Marque', 'Service', 'Emplacement']

class SearchForm(forms.Form):
    query = forms.CharField(label='Recherche', max_length=100, required=False)

class SoftwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ['NomEquipement', 'SystemeExploitation', 'Logiciel']
class SearchsForm(forms.Form):
    query = forms.CharField(label='Recherche', max_length=100, required=False)

class CapaciteForm(forms.ModelForm):
    class Meta:
        model = Capacite
        fields = ['NomEquipement', 'Ram', 'Processeur', 'Stockage']
