from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Produit, Revendeur, Commande, Stock


@login_required(login_url='login')
def dashboard(request):
    total_in_stock = Stock.objects.filter(disponibilite__gt=0).count()
    total_out_stock = Stock.objects.filter(disponibilite__lt=1).count()
    total_product = Produit.objects.count()
    total_supplier = Revendeur.objects.count()
    total_pending_order = Commande.objects.filter(status='pending').count()
    total_order = Commande.objects.filter(status='complete').count()
    orders = Commande.objects.filter(status='pending').order_by('-id')
    out_of_stock = Stock.objects.filter(disponibilite=0).order_by('-produit')
    context = {
        'produit': total_product,
        'total_in_stock': total_in_stock,
        'total_out_stock': total_out_stock,
        'revendeur': total_supplier,
        'pending_order': total_pending_order,
        'completed_order': total_order,
        'orders': orders,
        'out_of_stock': out_of_stock,

    }
    return render(request, 'dashboard.html', context)
