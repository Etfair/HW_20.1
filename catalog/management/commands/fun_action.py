from django.core.management import BaseCommand

from catalog.models import Category, Product
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('data.json') as file:
            content = json.load(file)

        categories_for_create = []
        products_for_create = []

        for data in content:
            if data['model'] == 'catalog.category':
                categories_for_create.append(Category(pk=data['pk'],
                                                      name=data['fields']['name'],
                                                      description=data['fields']['description']))
            elif data['model'] == 'catalog.product':
                products_for_create.append(Product(name=data['fields']['name'],
                                                   description=data['fields']['description'],
                                                   image=data['fields']['image'],
                                                   price=data['fields']['price'],
                                                   category=data['fields']['category']))
            else:
                continue

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)

        Product.objects.all().delete()
        Product.objects.bulk_create(products_for_create)
