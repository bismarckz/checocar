# Generated by Django 3.0.5 on 2020-04-29 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200421_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='cantidad',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
