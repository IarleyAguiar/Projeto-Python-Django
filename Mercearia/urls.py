from django.urls import path
from . import views

urlpatterns=[
    path("", views.ver_preco, name="index"),
    path("compra.html", views.compras, name="compra")
]