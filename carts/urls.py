from django.urls import path

from carts import views

app_name = "carts"

urlpatterns = [
    path("cart_add/<int:product_id>/", views.cart_add, name="cart_add"),
    path("cart_change/<int:product_id>/", views.cart_change, name="cart_change"),
    path("cart_delete/<int:product_id>/", views.cart_delete, name="cart_delete"),
]
