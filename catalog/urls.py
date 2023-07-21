from django.urls import path

from catalog.views import HomeListView, CategoryListView, ProductListView


urlpatterns = [
    path('', HomeListView.as_view(), name='product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/<int:pk>/', ProductListView.as_view(), name='categories_product'),
]
