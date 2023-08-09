# Generated by Django 4.2.3 on 2023-08-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rnd_key',
            field=models.IntegerField(default=0, verbose_name='ключ для верификации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]