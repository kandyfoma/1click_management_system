from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Season,
    Department,
    Product,
    Order,
    Delivery,
    Stock
)
from .forms import (
    SupplierForm,
    SeasonForm,
    DepartmentForm,
    ProductForm,
    OrderForm,
    DeliveryForm,
    StockForm,
    OrderUpdateForm)


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            Supplier.objects.create(name=name, address=address)
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSupplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Season views
@login_required(login_url='login')
def create_season(request):
    forms = SeasonForm()
    if request.method == 'POST':
        forms = SeasonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('season-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSeason.html', context)


class SeasonListView(ListView):
    model = Season
    template_name = 'store/season_list.html'
    context_object_name = 'season'


# Drop views
@login_required(login_url='login')
def create_department(request):
    forms = DepartmentForm()
    if request.method == 'POST':
        forms = DepartmentForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('department-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCategory.html', context)


class DepartmentListView(ListView):
    model = Department
    template_name = 'store/category_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addProduct.html', context)


class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            amount = forms.cleaned_data['amount']
            order_number = forms.cleaned_data['order_number']
            department = forms.cleaned_data['department']
            season = forms.cleaned_data['season']
            created_by = request.user
            Order.objects.create(
                supplier=supplier,
                product=product,
                amount=amount,
                order_number=order_number,
                department=department,
                season=season,
                created_by=created_by,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addOrder.html', context)


# Update Order details
@login_required(login_url='login')
def update_order(request, id):
    # dictionary for initial data with
    # field names as keys
    # fetch the object related to passed id
    obj = get_object_or_404(Order, id=id)
    form = OrderUpdateForm(request.POST or None, instance=obj)

    # pass the object as instance in form

    if request.method == 'POST':
        if form.is_valid():
            # update the existing `Band` in the database
            form.save()
            # redirect to the detail page of the `Band` we just updated
            return redirect('order-list')
        else:
            form = OrderUpdateForm(instance=obj)

    return render(request, 'store/updateOrder.html', {'form': form})


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-product')
        return context


# Update Stock details
@login_required(login_url='login')
def update_delivery(request, id):
    # dictionary for initial data with
    # field names as keys
    # fetch the object related to passed id
    obj = get_object_or_404(Delivery, id=id)
    form = DeliveryForm(request.POST or None, instance=obj)

    # pass the object as instance in form

    if request.method == 'POST':
        if form.is_valid():
            # update the existing `Stock` in the database
            form.save()
            # redirect to the detail page of the `Stock` we just updated
            return redirect('delivery-list')
        else:
            form = StockForm(instance=obj)

    return render(request, 'store/updateDelivery.html', {'form': form})


class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'


# Update Stock details
@login_required(login_url='login')
def update_stock(request, id):
    # dictionary for initial data with
    # field names as keys
    # fetch the object related to passed id
    obj = get_object_or_404(Stock, id=id)
    form = StockForm(request.POST or None, instance=obj)

    # pass the object as instance in form

    if request.method == 'POST':
        if form.is_valid():
            # update the existing `Stock` in the database
            form.save()
            # redirect to the detail page of the `Stock` we just updated
            return redirect('stock-list')
        else:
            form = StockForm(instance=obj)

    return render(request, 'store/updateStock.html', {'form': form})


# Update Product details
@login_required(login_url='login')
def update_product(request, id):
    # dictionary for initial data with
    # field names as keys
    # fetch the object related to passed id
    obj = get_object_or_404(Stock, id=id)
    form = ProductForm(request.POST or None, instance=obj)

    # pass the object as instance in form

    if request.method == 'POST':
        if form.is_valid():
            # update the existing `Stock` in the database
            form.save()
            # redirect to the detail page of the `Stock` we just updated
            return redirect('stock-list')
        else:
            form = StockForm(instance=obj)

    return render(request, 'store/updateProduct.html', {'form': form})


class StockListView(ListView):
    model = Stock
    template_name = 'store/stock_list.html'
    context_object_name = 'stock'
