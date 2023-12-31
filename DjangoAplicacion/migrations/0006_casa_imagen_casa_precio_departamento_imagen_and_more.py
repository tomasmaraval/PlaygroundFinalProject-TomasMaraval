# Generated by Django 4.2.7 on 2023-11-30 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoAplicacion', '0005_casa_departamento_delete_curso_delete_profesor'),
    ]

    operations = [
        migrations.AddField(
            model_name='casa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='casas'),
        ),
        migrations.AddField(
            model_name='casa',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='departamento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='departamentos'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
