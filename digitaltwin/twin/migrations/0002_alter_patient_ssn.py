# Generated by Django 3.2.7 on 2021-09-25 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='ssn',
            field=models.CharField(max_length=30, verbose_name='SSN'),
        ),
    ]
