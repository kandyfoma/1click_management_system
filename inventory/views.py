from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from store.models import Product, Supplier, Order, Stock


@login_required(login_url='login')
def dashboard(request):
    total_in_stock = Stock.objects.filter(availability__gt=0).count()
    total_out_stock = Stock.objects.filter(availability__lt=1).count()
    total_product = Product.objects.count()
    total_supplier = Supplier.objects.count()
    total_pending_order = Order.objects.filter(status='pending').count()
    total_order = Order.objects.filter(status='complete').count()
    orders = Order.objects.filter(status='pending').order_by('-id')
    out_of_stock = Stock.objects.filter(availability=0).order_by('-product')
    context = {
        'product': total_product,
        'total_in_stock': total_in_stock,
        'total_out_stock': total_out_stock,
        'supplier': total_supplier,
        'pending_order': total_pending_order,
        'completed_order': total_order,
        'orders': orders,
        'out_of_stock': out_of_stock,

    }
    return render(request, 'dashboard.html', context)
