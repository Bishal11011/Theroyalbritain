# Generated by Django 3.2.7 on 2021-09-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210920_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='festivals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
