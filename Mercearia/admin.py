from django.contrib import admin
from .models import Mercearia

@admin.register(Mercearia)
class MerceariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'entrega', 'total', 'id')

