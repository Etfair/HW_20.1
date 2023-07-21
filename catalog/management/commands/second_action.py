from django.core.management import BaseCommand

from catalog.models import Product
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('data.json') as file:
            content = json.load(file)

        products_for_create = []

        for data in content:
            if data['model'] == 'catalog.product':
                products_for_create.append(Product(name=data['fields']['name'],
                                                   description=data['fields']['description'],
                                                   image=data['fields']['image'],
                                                   category_id=data['fields']['category'],
                                                   price=data['fields']['price'],
                                                   date_create=data['fields']['date_create'],
                                                   date_last_fix=data['fields']['date_last_fix']))

            else:
                continue

        Product.objects.all().delete()
        # Product.objects.bulk_create(products_for_create)
