# Generated by Django 4.2.2 on 2023-06-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticacao', '0002_alter_users_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
