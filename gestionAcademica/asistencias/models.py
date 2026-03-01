from django.db import models
import uuid

# Create your models here.
class Asistencia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField(auto_now=True)
    confirmacion = models.BooleanField(default=False)
    id_inscripcion = models.ForeignKey('inscripciones.Inscripcion', on_delete=models.CASCADE)   

    def __str__(self):
        return f"ID: {self.id} - Fecha: {self.fecha} - Confirmacion: {self.confirmacion} - Inscripcion: {self.id_inscripcion}"