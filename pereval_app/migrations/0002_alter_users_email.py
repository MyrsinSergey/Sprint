# Generated by Django 4.2.3 on 2023-07-20 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pereval_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.EmailField(max_length=30, verbose_name='Электронная почта'),
        ),
    ]
