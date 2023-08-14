from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from catalog.forms import ProductForm, CategoryForm, VersionForm
from catalog.models import Product, Category, Version
from catalog.services import get_cached_subjects_for_product, get_cached_subjects_for_categories


class CategoryListView(ListView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/category_list.html'
    get_cached_subjects_for_categories()


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'

    def get_success_url(self):
        return reverse('view_product', args=[self.object.pk])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = ['catalog.set_published',
                           'catalog.change_prod_description',
                           'catalog.change_category_id',
                           'catalog.change_product'
                           ]

    def get_success_url(self):
        return reverse('view_product', args=[self.object.pk])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

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
    permission_required = 'catalog.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(category_id=self.kwargs.get('pk'))
        queryset = queryset.filter(
            category_id=self.kwargs.get('pk')
        )
        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Продукты, категории {category_item.name}'

        return context_data


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    permission_required = 'catalog.view_product'

    def get_context_data(self, subject_list=None, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['subjects'] = get_cached_subjects_for_product()
        return context_data


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'

    def get_success_url(self):
        return reverse('product')
