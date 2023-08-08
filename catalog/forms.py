from django import forms
from django.forms import BaseInlineFormSet

from catalog.models import Product, Category, Version

STOP_LIST = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        for word in STOP_LIST:
            if word in name:
                raise forms.ValidationError('Использование запрещенного слова')

            return name


class CategoryForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
        include = 'product'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name == 'last_vers':
                field.widget.attrs['class'] = 'form-chek-input'
            else:
                field.widget.attrs['class'] = 'form-control'


