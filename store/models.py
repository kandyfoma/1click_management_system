from django.db import models

from users.models import User


class Revendeur(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    adresse = models.CharField(max_length=220, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Saison(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    cree_par = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='cree_par_saison')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_saison')

    def __str__(self):
        return self.nom


class Departement(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)
    cree_par = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='cree_par_departement')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_departement')

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=120, unique=True)
    prix = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    cree_par = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='cree_par_produit')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_produit')

    def __str__(self):
        return self.nom


class Commande(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    numero_reference = models.PositiveIntegerField()
    revendeur = models.ForeignKey(Revendeur, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    montant = models.PositiveIntegerField()
    saison = models.ForeignKey(Saison, on_delete=models.CASCADE, null=True)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    cree_par = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='cree_par_order')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_order')

    def __str__(self):
        return self.produit.nom


class Delivery(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    courier_nom = models.CharField(max_length=120, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    cree_par = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='cree_par_delivery')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_delivery')

    def __str__(self):
        return self.courier_nom


class Stock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)
    stock_initiale = models.PositiveIntegerField(blank=True, null=True)
    disponibilite = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    cree_par = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='cree_par_stock')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_stock')

    def __str__(self):
        return self.produit.nom
