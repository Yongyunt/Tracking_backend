# Generated by Django 3.1.1 on 2020-10-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informationPer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='criterion',
            name='Works',
        ),
        migrations.AlterField(
            model_name='criterion',
            name='Research_level',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='criterion',
            name='book',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='personnel_information',
            name='Phone_number',
            field=models.IntegerField(max_length=10),
        ),
    ]