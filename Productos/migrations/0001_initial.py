# Generated by Django 5.0.3 on 2024-03-29 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id_categoria_cat', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cat', models.CharField(max_length=50)),
                ('descripcion_cat', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id_producto_pro', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pro', models.CharField(max_length=50)),
                ('descripcion_pro', models.TextField()),
                ('existencia_pro', models.IntegerField()),
                ('precio_pro', models.ImageField(max_length=9, upload_to='')),
                ('categoria_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Productos.categoria')),
            ],
        ),
    ]
