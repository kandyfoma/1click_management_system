from django.db import models

from users.models import User


class Supplier(models.Model):
    name = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=220, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=120, unique=True)
    description = models.CharField(max_length=220, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_by_season')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_season')

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=120, unique=True)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_by_department')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_department')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    price = models.PositiveIntegerField()
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_by_product')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_product')

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
        ('bulk', 'Bulk'),
    )
    order_number = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_by_order')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_order')

    def __str__(self):
        return 'Product: {}'.format(self.product.name)


class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    courier_name = models.CharField(max_length=120, blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_by_delivery')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_delivery')

    def __str__(self):
        return self.courier_name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    initial_in_stock = models.PositiveIntegerField(blank=True, null=True)
    availability = models.PositiveIntegerField(blank=True, null=True)
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='created_by_stock')
    updated_by = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True,
                                   related_name='updated_by_stock')

    def __str__(self):
        return self.product.name
