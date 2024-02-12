from django import forms

from catalog.constants import FORBIDDEN_WORDS
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        if kwargs.get('request'):
            del kwargs['request']
        super(ProductForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['name', 'description', 'img', 'category', 'price']

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Warning! Forbidden words in product name!')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Warning! Forbidden words in product description!')
        return cleaned_data

    def save(self, commit=True):
        product = super().save(commit=False)
        if self.user:
            product.user = self.user
        if commit:
            product.save()
        return product


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
