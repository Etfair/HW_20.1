from django.db import models

# Create your models here.
NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование')
    description = models.CharField(max_length=150, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория товара')
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_create = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_last_fix = models.DateTimeField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}\n Категория: {self.category} \nЦена: {self.price}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Категория')
    description = models.TextField(**NULLABLE, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

