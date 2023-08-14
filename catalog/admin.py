from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category', 'is_published', 'owner', 'description',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_vers', 'name_vers', 'last_vers',)
    list_filter = ('product',)
