from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('show/product/data', views.getProductData),
    path('add/item', views.addIteam),
    path('add/product', views.addProduct),
]
