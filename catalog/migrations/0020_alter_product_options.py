# Generated by Django 4.2.3 on 2023-08-11 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published', 'Can publish posts'), ('change_prod_description', 'change product description'), ('change_category_id', 'change category')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]
