from django.urls import path 
from . import views

urlpatterns = [
    path("products", views.products, name="products"),
    path("product_detail/<slug:slug>", views.product_detail, name="product_detail"),
    path("add_item/", views.add_item, name = "add_item")
]

# fetching all_products: http://127.0.0.1:8001/products


