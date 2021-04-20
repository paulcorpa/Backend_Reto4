from django.db import models

# Create your models here.
class AnimalModel(models.Model):
    animalId = models.AutoField(
      primary_key= True,
      null = False,
      unique = True,
      db_column= 'id'
    ) 
    animalEspecie = models.CharField(
      max_length= 45,
      null = False,
      db_column = 'especie',
      verbose_name= 'especie'
    )
    animalNombre = models.CharField(
      max_length= 45,
      null = False,
      db_column = 'nombre',
      help_text= 'Nombre del animal',
      verbose_name= 'nombre'
    )
    animalEdad = models.IntegerField(
      db_column= 'edad',
      null= False,
      verbose_name='edad'
    )
    class Meta:
      db_table = 'animales'
