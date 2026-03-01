import uuid
from django.db import models

# Create your models here.

class notas(models.Model):
	id_nota = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
	id_inscripcion = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	nota = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)
	corte = models.IntegerField(null=False, blank=False)
	fecha_registro = models.DateTimeField(auto_now_add=True)
	observaciones = models.TextField(blank=True, help_text="Observaciones del profesor")

	def __str__(self):
		return f"Nota: {self.nota}"