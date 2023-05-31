from django.urls import path
from . import views

urlpatterns=[
    path("ver/", views.ver_preco, name="ver_mercearia")
]