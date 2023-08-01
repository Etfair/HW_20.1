from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductForm, CategoryForm, VersionForm
from catalog.models import Product, Category, Version


class CategoryListView(ListView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('view_product', args=[self.object.pk])


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('view_product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home_list.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home_list.html'

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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog/home_list.html')


