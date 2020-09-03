from django.db import models
from django.utils import timezone

class Post(models.Model):
	titulo = models.CharField(max_length=200)
	fecha_de_publicacion = models.DateTimeField(default=timezone.now)

	definicion = models.TextField(blank=True)
	explicacion = models.TextField(blank=True)
	herramientas = models.TextField(blank=True)

	paso1 = models.TextField(blank=True)
	paso2 = models.TextField(blank=True)
	paso3 = models.TextField(blank=True)
	paso4 = models.TextField(blank=True)
	paso5 = models.TextField(blank=True)
	paso6 = models.TextField(blank=True)
	paso7 = models.TextField(blank=True)
	paso8 = models.TextField(blank=True)
	paso9 = models.TextField(blank=True)
	paso10 = models.TextField(blank=True)
	paso11 = models.TextField(blank=True)
	paso12 = models.TextField(blank=True)
	paso13 = models.TextField(blank=True)
	paso14 = models.TextField(blank=True)
	paso15 = models.TextField(blank=True)
	paso16 = models.TextField(blank=True)
	paso17 = models.TextField(blank=True)
	paso18 = models.TextField(blank=True)
	paso19 = models.TextField(blank=True)
	paso20 = models.TextField(blank=True)
	
	conclusiones = models.TextField(blank=True)
	#categorias = models.CharField(max_length=200)

	def publicar(self):
		self.save()

	def __str__(self):
		return self.titulo
