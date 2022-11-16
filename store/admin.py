from django.contrib import admin

from .models import (
    Revendeur,
    Saison,
    Departement,
    Produit,
    Commande,
    Delivery,
    Stock
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['nom', 'address', 'created_date']
    readonly_fields = ('created_date',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'nom', 'address', 'created_date']
    readonly_fields = ('cree_par', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class SaisonAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description', 'cree_par', 'created_date']
    readonly_fields = ('cree_par', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['nom', 'cree_par', 'created_date']
    readonly_fields = ('cree_par', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prix', 'cree_par', 'created_date']
    readonly_fields = ('cree_par', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class OrderAdmin(admin.ModelAdmin):
    list_display = ['produit', 'montant', 'departement', 'saison', 'status', 'cree_par', 'created_date']
    readonly_fields = ('cree_par', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class StockAdmin(admin.ModelAdmin):
    list_display = ['produit', 'disponibilite', 'cree_par', 'created_date']
    readonly_fields = ('cree_par', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.cree_par = request.user
        else:
            obj.updated_by = request.user
        obj.save()


admin.site.register(Revendeur, SupplierAdmin)
admin.site.register(Saison, SaisonAdmin)
admin.site.register(Departement, DepartmentAdmin)
admin.site.register(Produit, ProductAdmin)
admin.site.register(Commande, OrderAdmin)
admin.site.register(Delivery)
admin.site.register(Stock, StockAdmin)
