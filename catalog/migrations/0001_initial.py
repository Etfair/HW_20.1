# Generated by Django 4.2.3 on 2023-07-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('description', models.CharField(max_length=150, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catalog/', verbose_name='Изображение')),
                ('category', models.CharField(max_length=50, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена за покупку')),
                ('date_create', models.DateTimeField(verbose_name='Дата создания')),
                ('date_last_fix', models.DateTimeField(verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]