from django.db import models
from django.contrib.auth.models import User

class Mensaje(models.Model):
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados', verbose_name='Remitente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos', verbose_name='Destinatario')
    asunto = models.CharField(max_length=200, verbose_name='Asunto')
    contenido = models.TextField(verbose_name='Contenido')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    leido = models.BooleanField(default=False, verbose_name='Leído')

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return f'{self.remitente} → {self.destinatario}: {self.asunto}'