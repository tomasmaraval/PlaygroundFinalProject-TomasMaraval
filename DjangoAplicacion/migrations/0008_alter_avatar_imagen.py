# Generated by Django 4.2.7 on 2023-12-01 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAplicacion', '0007_alter_casa_imagen_alter_departamento_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='5411.jpeg', null=True, upload_to='avatares'),
        ),
    ]