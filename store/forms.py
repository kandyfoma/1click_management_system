from django import forms

from .models import Season, Department, Product, Order, Delivery, Stock


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))


class SeasonForm(forms.ModelForm):
    class Meta:
        model = Season
        fields = ['name', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'description'})
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'})
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'product', 'amount', 'order_number', 'department', 'season']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'amount'}),
            'order_number': forms.NumberInput(attrs={'class': 'form-control', 'id': 'order_number'}),
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
            'season': forms.Select(attrs={'class': 'form-control', 'id': 'season'}),
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['supplier', 'product', 'amount', 'department', 'season', 'status']

        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'amount'}),
            'season': forms.Select(attrs={'class': 'form-control', 'id': 'season'}),
            'department': forms.Select(attrs={'class': 'form-control', 'id': 'department'}),
            'status': forms.Select(attrs={'class': 'form-control', 'id': 'status'}),
        }


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = '__all__'

        widgets = {
            'order': forms.Select(attrs={'readonly': 'readonly', 'class': 'form-control', 'id': 'order'}),
            'courier_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'courier_name'}),
        }


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['product', 'availability']

        widgets = {
            'product': forms.Select(attrs={'class': 'form-control', 'id': 'product'}),
            'availability': forms.NumberInput(attrs={'class': 'form-control', 'id': 'availability'}),
        }
