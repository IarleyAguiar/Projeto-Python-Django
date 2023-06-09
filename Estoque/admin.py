from django.contrib import admin
from .models import Arroz, Feijao, Refri

class Myadmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False
@admin.register(Arroz)
class ArrozAdmin(admin.ModelAdmin):
    list_display = ('nome_arroz', 'qtd_arroz', 'preco_arroz')

@admin.register(Feijao)
class FeijaoAdmin(admin.ModelAdmin):
    list_display = ('nome_feijao', 'qtd_feijao', 'preco_feijao')

@admin.register(Refri)
class RefriAdmin(admin.ModelAdmin):
    list_display = ('nome_refri', 'qtd_refri', 'preco_refri')

