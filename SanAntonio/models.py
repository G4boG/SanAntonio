from django.db import models
from django.core.validators import MinValueValidato

class Escolar(models.Model):
    OPCIONES_CATEGORIA = [
        ('TEXTO', 'Libros/Diccionarios'),
        ('TECNOLOGIA', 'Tablets/Proyectores'),
        ('OFICINa', 'Plastificadoras/Resmas')
    ]
    