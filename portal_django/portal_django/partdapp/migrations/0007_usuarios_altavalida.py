# Generated by Django 2.2.7 on 2020-05-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partdapp', '0006_usuarios_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='altavalida',
            field=models.CharField(default='NO', max_length=150),
        ),
    ]
