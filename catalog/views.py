from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product, Category


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/includes/category_list.html'


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/includes/home_list.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/includes/home_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Продукты, категории {category_item.name}'

        return context_data
