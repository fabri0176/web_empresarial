import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Nombre', max_length=100)
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["-created"] #ordenado de descendente -

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title  = models.CharField(verbose_name='Titulo', max_length=200)
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha Publicación', default = timezone.now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name = 'Autor', on_delete=models.CASCADE )
    categories = models.ManyToManyField(Category, verbose_name = 'Categorias')
    created = models.DateTimeField(verbose_name='Creado', auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"] #ordenado de descendente -


