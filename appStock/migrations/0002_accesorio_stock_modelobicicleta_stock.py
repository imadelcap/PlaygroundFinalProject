# Generated by Django 4.2.7 on 2023-12-19 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appStock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorio',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modelobicicleta',
            name='stock',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
