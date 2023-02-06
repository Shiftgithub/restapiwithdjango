from django.urls import path
from . import views

urlpatterns = [
    path('show/item/data', views.getData, name="show.items.data"),
    path('show/product/data', views.getProductData, name="show.products.data"),
    path('add/item', views.addIteam, name="add.item"),
    path('add/product', views.addProduct, name="add.product"),
]
