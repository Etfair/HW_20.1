from django.urls import path

from catalog.views import home, categories, categories_product


urlpatterns = [
    path('', home, name='product'),
    path('categories/', categories, name='categories'),
    path('<int:pk>/product/', categories_product, name='categories_product'),
]
