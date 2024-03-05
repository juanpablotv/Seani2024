from django.db import models

# Create your models here.
class Career(models.Model):
    
    LEVELS = [
        ('Ing', 'Ingeniería'),
        ('TSU', 'Tecnico Superior Universitario'),
        ('M', 'Maestría')
    ]
    
    level = models.IntegerField(
        verbose_name = 'Nivel',
        max_length = 10,
        choices = LEVELS)
    name = models.CharField(
        verbose_name = 'Nombre',
        max_length = 200)
    short_name = models.CharField(
        verbose_name = 'Abreviatura',
        max_length = 20)
    

    def __str__(self):
        return f"{ self.level } - { self.short_name }"

    class Meta:
        verbose_name = 'carrera'
        verbose_name_plural = 'carreras'