# Generated by Django 5.0.3 on 2024-05-01 00:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_producto_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_pro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Productos.categoria'),
        ),
    ]
