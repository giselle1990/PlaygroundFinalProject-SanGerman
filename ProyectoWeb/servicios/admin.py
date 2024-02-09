from django.contrib import admin

from .models import Servicio

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('updated', 'created')


admin.site.register(Servicio, ServicioAdmin)
