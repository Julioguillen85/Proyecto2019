from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 200, verbose_name="titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title

class Service(models.Model):
    title_service = models.CharField(max_length = 200, verbose_name="titulo")
    description_service = models.TextField(verbose_name="Descripcion")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
      

    def __str__(self):
        return self.title_service