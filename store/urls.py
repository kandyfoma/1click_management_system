from django.urls import path

from .views import (
    create_supplier,
    create_season,
    create_department,
    create_product,
    create_order,
    update_delivery,
    update_order,
    update_stock,
    update_product,

    SupplierListView,
    SeasonListView,
    DepartmentListView,
    ProductListView,
    OrderListView,
    DeliveryListView,
    StockListView,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-season/', create_season, name='create-season'),
    path('create-department/', create_department, name='create-department'),
    path('create-product/', create_product, name='create-product'),
    path('create-order/', create_order, name='create-order'),

    path('update-delivery/<int:id>/', update_delivery, name='update-delivery'),
    path('update-product/<int:id>/', update_product, name='update-product'),
    path('update-order/<int:id>/', update_order, name='update-order'),
    path('update-stock/<int:id>/', update_stock, name='update-stock'),

    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('season-list/', SeasonListView.as_view(), name='season-list'),
    path('department-list/', DepartmentListView.as_view(), name='department-list'),
    path('product-list/', ProductListView.as_view(), name='product-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('delivery-list/', DeliveryListView.as_view(), name='delivery-list'),
    path('stock-list/', StockListView.as_view(), name='stock-list'),
]
