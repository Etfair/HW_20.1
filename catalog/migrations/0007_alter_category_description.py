# Generated by Django 4.2.3 on 2023-07-13 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_category_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=50, verbose_name='Описание'),
        ),
    ]
