from django.apps import AppConfig


class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        from django.db.models.signals import post_save

        from store.signals.signals import create_delivery, create_stock
        from store.models import Order

        post_save.connect(create_delivery, sender=Order)
        post_save.connect(create_stock, sender=Order)