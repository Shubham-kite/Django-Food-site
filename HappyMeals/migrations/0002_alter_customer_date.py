# Generated by Django 3.2.5 on 2021-09-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyMeals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateField(),
        ),
    ]