from django.contrib import admin

# Register your models here.

from appStock.models import ModeloBicicleta, Accesorio

admin.site.register(ModeloBicicleta)
admin.site.register(Accesorio)