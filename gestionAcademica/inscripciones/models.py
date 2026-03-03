import uuid
from django.db import models

class Inscripcion(models.Model):
    id_inscripcion = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, 
                                      primary_key=True)
    id_estudiante = models.BigIntegerField(unique=True, db_index=True)
    id_materia = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, default='ACTIVA')
