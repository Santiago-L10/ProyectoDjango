from django.db import models
import uuid

# Create your models here.
class Materia(models.Model):

    id_materia = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField(default=3)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre