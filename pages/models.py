from django.db import models

# Create your models here.


class Page(models.Model):

    title = models.CharField(verbose_name="Título", max_length=200)
    content = models.TextField(verbose_name="Contenido")
    created = models.DateField(auto_now_add=True, verbose_name="Fecha creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['title']

    def __str__(self) -> str:
        return f'{self.id} - {self.title}'
