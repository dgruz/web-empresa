from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length =200, verbose_name = "Título")
    subtitle = models.CharField(max_length =200,verbose_name = "Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name = "Imagen",upload_to="services")
    created = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Fecha de Edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title

"""
class MyUser(User):
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    REQUIRED_FIELDS = ['date_of_birth', 'height']

"""
