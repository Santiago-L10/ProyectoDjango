import uuid
from django.db import models

class Rol(models.Model):
    id_rol = models.UUIDField(default = uuid.uuid4, unique=True, editable=False, 
                              primary_key=True)
    nombre_rol =models.CharField(max_length=20)


class TipoDocumento(models.Model):
    id_tipo_doc = models.UUIDField(default = uuid.uuid4, unique=True, editable=False, 
                              primary_key=True)
    nombre_tipo_doc =models.CharField(max_length=20)


class Usuario(models.Model):
    id_usuario = models.BigIntegerField(unique=True, db_index=True, primary_key=True)
    nombre_usuario = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)
    id_tipo_documento = models.ForeignKey(
        TipoDocumento,
        on_delete=models.PROTECT,
        related_name="tiposDocumento",
        related_query_name="tipoDocumento"
    )
    id_rol = models.ForeignKey(
        Rol,
        on_delete=models.PROTECT,
        related_name="roles",
        related_query_name="rol"
    )
    
