# Generated by Django 4.2.3 on 2023-07-31 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_rename_equipos_equipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alquiler',
            old_name='potencia',
            new_name='precio',
        ),
    ]
