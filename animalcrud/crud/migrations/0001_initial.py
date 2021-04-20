# Generated by Django 3.2 on 2021-04-20 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalModel',
            fields=[
                ('animalId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('animalEspecie', models.CharField(db_column='especie', max_length=45, verbose_name='especie')),
                ('animalNombre', models.CharField(db_column='nombre', help_text='Nombre del animal', max_length=45, verbose_name='nombre')),
                ('animalEdad', models.IntegerField(db_column='edad')),
            ],
            options={
                'db_table': 'animales',
            },
        ),
    ]