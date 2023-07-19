from django.core.management import BaseCommand

from catalog.models import Category
import json


class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('data.json') as file:
            content = json.load(file)

        categories_for_create = []

        for data in content:
            if data['model'] == 'catalog.category':
                categories_for_create.append(Category(pk=data['pk'],
                                                      name=data['fields']['name'],
                                                      description=data['fields']['description']))

            else:
                continue

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_for_create)
