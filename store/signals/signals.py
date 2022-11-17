import logging

from django.conf import settings

from store.models import Delivery, Stock

logger = logging.getLogger(__name__)


def create_delivery(sender, instance, **kwargs):
    if instance.status == 'complete':
        Delivery.objects.create(commande=instance)


def create_stock(sender, instance, **kwargs):
    if instance.status == 'complete':
        product_in_stock = Stock.objects.filter(produit=instance.produit).first()
        if product_in_stock:
            product_in_stock.initial_in_stock = product_in_stock.initial_in_stock + instance.amount
            product_in_stock.availability = instance.amount
            product_in_stock.save()
        else:
            Stock.objects.create(produit=instance.produit, stock_initiale=instance.montant,
                                 disponibilite=instance.montant)
