from django.urls import path

from catalog.views import HomeListView, CategoryListView, ProductListView,\
    ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView


urlpatterns = [
    path('', HomeListView.as_view(), name='product'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/<int:pk>/', ProductListView.as_view(), name='categories_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('view/<int:pk>/', (ProductDetailView.as_view()), name='view_product'),
]
