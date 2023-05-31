from django.contrib import admin
from .models import Mercearia
from django.contrib.auth.models import Group  # new
admin.site.unregister(Group)


@admin.register(Mercearia)
class MerceariaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'total', 'id')

