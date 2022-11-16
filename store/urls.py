from django.urls import path

from .views import (
    create_revendeur,
    create_saison,
    create_department,
    create_product,
    create_order,
    update_delivery,
    update_order,
    update_stock,
    update_product,

    RevendeurListView,
    SaisonListView,
    DepartmentListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
    StockListView,
)

urlpatterns = [
    path('create-revendeur/', create_revendeur, name='create-revendeur'),
    path('create-season/', create_saison, name='create-saison'),
    path('create-department/', create_department, name='create-department'),
    path('create-produit/', create_product, name='create-produit'),
    path('create-commande/', create_order, name='create-commande'),

    path('update-delivery/<int:id>/', update_delivery, name='update-delivery'),
    path('update-produit/<int:id>/', update_product, name='update-produit'),
    path('update-commande/<int:id>/', update_order, name='update-commande'),
    path('update-stock/<int:id>/', update_stock, name='update-stock'),

    path('revendeur-list/', RevendeurListView.as_view(), name='revendeur-list'),
    path('season-list/', SaisonListView.as_view(), name='saison-list'),
    path('department-list/', DepartmentListView.as_view(), name='department-list'),
    path('produit-list/', ProductListView.as_view(), name='produit-list'),
    path('commande-list/', OrderListView.as_view(), name='commande-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('stock-list/', StockListView.as_view(), name='stock-list'),
]
