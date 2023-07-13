from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Котлеты', 'description': 'Мясные', 'category': 'Полуфабрикат', 'price': 120},
            {'name': 'Стейк', 'description': 'Говядина', 'category': 'Полуфабрикат', 'price': 170},
            {'name': 'Картофель', 'description': 'Новый урожай', 'category': 'Овощи', 'price': 19},
            {'name': 'Сырники', 'description': 'На завтрак', 'category': 'Полуфабрикат', 'price': 75},
            {'name': 'Лук', 'description': 'Новый урожай', 'category': 'Овощи', 'price': 15},
            {'name': 'Перец', 'description': 'Болгарский', 'category': 'Овощи', 'price': 37},
            {'name': 'яблоки', 'description': 'Сезонные', 'category': 'фрукты', 'price': 31},
        ]

        # for product_item in product_list:
        #     Product.objects.create(**product_item)

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product(**product_item)
            )
        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
