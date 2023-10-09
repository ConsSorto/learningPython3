from django.db import models

# Create your models here.
class Article(models.Model):
    tittle = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    public = models.BooleanField(verbose_name="Esta publicado")
    image = models.ImageField(default='null', verbose_name="Imagen del articulo", upload_to="articles")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=["-id"]
    def __str__(self):
        return f"{self.tittle} ({self.id}))"
        
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    descripton = models.CharField(max_length=100, verbose_name="Descripcion")
    created_at = models.DateField(verbose_name="Fecha de Creacion")

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias"
        ordering=["-id"]
