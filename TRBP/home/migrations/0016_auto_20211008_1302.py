# Generated by Django 3.2.7 on 2021-10-08 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20211008_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='trip',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trips_review', to='home.trips'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='pay',
            field=models.CharField(blank=True, choices=[('Cash', 'Cash'), ('Traveller Cheque', 'Traveller Cheque'), ('Credit Card', 'Credit Card'), ('Bank Transfer', 'Bank Transfer')], default=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='salutation',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Miss.', 'Miss.'), ('Mr.', 'Mr.')], default='Mr.', max_length=20, null=True),
        ),
    ]
