# Generated by Django 4.2.3 on 2023-07-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('Content', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(upload_to='blog/', verbose_name='Изображение')),
                ('date_of_creation', models.DateTimeField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Материал',
                'verbose_name_plural': 'Материалы',
            },
        ),
    ]
