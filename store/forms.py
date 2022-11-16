from django import forms

from .models import Saison, Departement, Produit, Commande, Delivery, Stock


class RevendeurForm(forms.Form):
    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'nom',
        'data-val': 'true',
        'data-val-required': 'Veillez completer nom',
    }))
    adresse = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'adresse',
        'data-val': 'true',
        'data-val-required': 'Veillez completer adresse',
    }))


class SaisonForm(forms.ModelForm):
    class Meta:
        model = Saison
        fields = ['nom', 'description']

        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'nom'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
        }


class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'nom'})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'prix']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'nom'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'id': 'prix'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['revendeur', 'produit', 'montant', 'numero_reference', 'departement', 'saison']

        widgets = {
            'revendeur': forms.Select(attrs={'class': 'form-control', 'id': 'revendeur'}),
            'produit': forms.Select(attrs={'class': 'form-control', 'id': 'produit'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'id': 'montant'}),
            'numero_reference': forms.NumberInput(attrs={'class': 'form-control', 'id': 'numero_reference'}),
            'departement': forms.Select(attrs={'class': 'form-control', 'id': 'departement'}),
            'saison': forms.Select(attrs={'class': 'form-control', 'id': 'saison'}),
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['revendeur', 'produit', 'montant', 'departement', 'saison', 'status']

        widgets = {
            'revendeur': forms.Select(attrs={'class': 'form-control', 'id': 'revendeur'}),
            'produit': forms.Select(attrs={'class': 'form-control', 'id': 'produit'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control', 'id': 'montant'}),
            'saison': forms.Select(attrs={'class': 'form-control', 'id': 'saison'}),
            'departement': forms.Select(attrs={'class': 'form-control', 'id': 'departement'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'status'}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'commande': forms.Select(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'commande'}),
            'courier_nom': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_nom'}),
        }


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['produit', 'disponibilite']

        widgets = {
            'produit': forms.Select(attrs={'class': 'form-control', 'id': 'produit'}),
            'disponibilite': forms.NumberInput(attrs={'class': 'form-control', 'id': 'disponibilite'}),
        }
