# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EjercicioDeEntrenamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serie', models.IntegerField()),
                ('repeticiones', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('ejercicio', models.ForeignKey(to='registro.Ejercicio')),
            ],
        ),
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='EntrenamientoDeRutina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('entrenamiento', models.ForeignKey(to='registro.Entrenamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Menudeo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio', models.FloatField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Musculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.BooleanField()),
                ('valor', models.FloatField()),
                ('fecha_realizacion', models.DateField()),
                ('fecha_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('primerApellido', models.CharField(max_length=30)),
                ('segundoApellido', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateField()),
                ('fechaIngreso', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('existencias', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Rutina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('valor', models.FloatField()),
                ('estado', models.BooleanField()),
                ('descripcion', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='registro.Persona')),
            ],
            bases=('registro.persona',),
        ),
        migrations.AddField(
            model_name='pago',
            name='tipoPago',
            field=models.ForeignKey(to='registro.TipoPago'),
        ),
        migrations.AddField(
            model_name='menudeo',
            name='producto',
            field=models.ForeignKey(to='registro.Producto'),
        ),
        migrations.AddField(
            model_name='entrenamientoderutina',
            name='rutina',
            field=models.ForeignKey(to='registro.Rutina'),
        ),
        migrations.AddField(
            model_name='entrenamiento',
            name='musculo',
            field=models.ForeignKey(to='registro.Musculo'),
        ),
        migrations.AddField(
            model_name='ejerciciodeentrenamiento',
            name='entrenamiento',
            field=models.ForeignKey(to='registro.Entrenamiento'),
        ),
        migrations.AddField(
            model_name='compra',
            name='menudeo',
            field=models.ForeignKey(to='registro.Menudeo'),
        ),
        migrations.AddField(
            model_name='pago',
            name='cliente',
            field=models.ForeignKey(to='registro.Cliente'),
        ),
    ]
