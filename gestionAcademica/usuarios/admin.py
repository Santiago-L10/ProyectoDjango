from django.contrib import admin
from .models import Usuario, Rol, TipoDocumento

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(TipoDocumento)