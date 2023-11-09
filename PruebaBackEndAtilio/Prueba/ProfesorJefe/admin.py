from django.contrib import admin
from ProfesorJefe.models import ProfJefe

class ProfeAdmin(admin.ModelAdmin):
    list_display = ['nombre','correo','telefono']

admin.site.register(ProfJefe)
# Register your models here.

# Register your models here.
