# Generated by Django 4.2.3 on 2023-07-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_username_recipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(help_text='in minutes'),
        ),
    ]
