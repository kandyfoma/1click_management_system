from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Revendeur,
    Saison,
    Departement,
    Produit,
    Commande,
    Delivery,
    Stock
)
from .forms import (
    RevendeurForm,
    SaisonForm,
    DepartementForm,
    ProductForm,
    OrderForm,
    DeliveryForm,
    StockForm,
    OrderUpdateForm)


# Revendeur views
@login_required(login_url='login')
def create_revendeur(request):
    forms = RevendeurForm()
    if request.method == 'POST':
        forms = RevendeurForm(request.POST)
        if forms.is_valid():
            nom = forms.cleaned_data['nom']
            adresse = forms.cleaned_data['adresse']
            Revendeur.objects.create(nom=nom, adresse=adresse)
            return redirect('revendeur-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSupplier.html', context)


class RevendeurListView(ListView):
    model = Revendeur
    template_nom = 'store/revendeur_list.html'
    context_object_nom = 'revendeur'


# saison views
@login_required(login_url='login')
def create_saison(request):
    forms = SaisonForm()
    if request.method == 'POST':
        forms = SaisonForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('saison-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addSeason.html', context)


class SaisonListView(ListView):
    model = Saison
    template_nom = 'store/saison_list.html'
    context_object_nom = 'saison'


# Drop views
@login_required(login_url='login')
def create_department(request):
    forms = DepartementForm()
    if request.method == 'POST':
        forms = DepartementForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('department-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addCategory.html', context)


class DepartmentListView(ListView):
    model = Departement
    template_nom = 'store/category_list.html'
    context_object_nom = 'drop'


# Produit views
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
    model = Produit
    template_nom = 'store/product_list.html'
    context_object_nom = 'produit'


# Commande views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            revendeur = forms.cleaned_data['revendeur']
            product = forms.cleaned_data['produit']
            amount = forms.cleaned_data['montant']
            order_number = forms.cleaned_data['numero_reference']
            department = forms.cleaned_data['department']
            saison = forms.cleaned_data['saison']
            cree_par = request.user
            Commande.objects.create(
                revendeur=revendeur,
                product=product,
                amount=amount,
                order_number=order_number,
                department=department,
                saison=saison,
                cree_par=cree_par,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/addOrder.html', context)


# Update Commande details
@login_required(login_url='login')
def update_order(request, id):
    # dictionary for initial data with
    # field noms as keys
    # fetch the object related to passed id
    obj = get_object_or_404(Commande, id=id)
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
    model = Commande
    template_nom = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['commande'] = Commande.objects.all().order_by('-produit')
        return context


# Update Stock details
@login_required(login_url='login')
def update_delivery(request, id):
    # dictionary for initial data with
    # field noms as keys
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
    template_nom = 'store/delivery_list.html'
    context_object_nom = 'delivery'


# Update Stock details
@login_required(login_url='login')
def update_stock(request, id):
    # dictionary for initial data with
    # field noms as keys
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


# Update Produit details
@login_required(login_url='login')
def update_product(request, id):
    # dictionary for initial data with
    # field noms as keys
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
    template_nom = 'store/stock_list.html'
    context_object_nom = 'stock'
