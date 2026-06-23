from django.db import models
from django.core.validators import MinValueValidator
class Escolar(models.Model):
    OPCIONES_CATEGORIA = [
        ('TEXTO', 'Libros/Diccionarios'),
        ('TECNOLOGIA', 'Tablets/Proyectores'),
        ('OFICINa', 'Plastificadoras/Resmas')
    ]
    
    nombre = models.CharField(max_length=100)

    categoria = models.CharField(
        max_length=20,
        choices=OPCIONES_CATEGORIA,
        default='TEXTO'
    )
    
    stock = models.IntegerField(validators=[MinValueValidator(0,message="el stock no puede ser negativo")])

    ubicacion = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.nombre} ({self.get_categoria_display()})"