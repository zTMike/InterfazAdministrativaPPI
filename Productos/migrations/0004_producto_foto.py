# Generated by Django 5.0.3 on 2024-03-30 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0003_alter_producto_precio_pro'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]
