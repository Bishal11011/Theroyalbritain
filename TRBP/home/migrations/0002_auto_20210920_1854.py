# Generated by Django 3.2.7 on 2021-09-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='festivals',
            name='discription',
        ),
        migrations.RemoveField(
            model_name='festivals',
            name='photo',
        ),
        migrations.AddField(
            model_name='festivals',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='festivals',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='festivals',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]