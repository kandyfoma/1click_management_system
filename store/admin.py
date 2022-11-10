from django.contrib import admin

from .models import (
    Supplier,
    Season,
    Department,
    Product,
    Order,
    Delivery,
    Stock
)


class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'created_date']
    readonly_fields = ('created_date',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class BuyerAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'address', 'created_date']
    readonly_fields = ('created_by', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_by', 'created_date']
    readonly_fields = ('created_by', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'created_date']
    readonly_fields = ('created_by', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sortno', 'price', 'created_by', 'created_date']
    readonly_fields = ('created_by', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'amount', 'department', 'season', 'status', 'created_by', 'created_date']
    readonly_fields = ('created_by', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


class StockAdmin(admin.ModelAdmin):
    list_display = ['product', 'availability', 'created_by', 'created_date']
    readonly_fields = ('created_by', 'updated_by', 'created_date')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        else:
            obj.updated_by = request.user
        obj.save()


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery)
admin.site.register(Stock, StockAdmin)
