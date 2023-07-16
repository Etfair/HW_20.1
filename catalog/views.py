from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.


def categories(request):
    context = {
        'object_list': Category.objects.all()
    }
    return render(request, 'main/categories.html', context)


def home(request):
    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'main/home.html', context)


def categories_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Продукты, категории {category_item.name}'
    }
    return render(request, 'main/home.html', context)
