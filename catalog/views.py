from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from catalog.forms import ProductForm, VersionForm, ModeratedProductForm
from catalog.models import Product, Version, Category


class CatalogListView(ListView):
    model = Product
    extra_context = {'title': 'catalog'}


class ProductDetailView(DetailView):

    model = Product
    extra_context = {'title': 'product'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'product'
        context['product_pk'] = self.object.pk
        active_version = Version.objects.filter(product=self.object.pk, is_active=True)
        if active_version:
            context['active_version'] = active_version[0]
        return context

    @method_decorator(cache_page(60 * 15))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog')
    extra_context = {'title': 'new product'}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'
    success_url = reverse_lazy('catalog:catalog')
    template_name = 'catalog/product_update.html'

    def get_form_class(self):

        if ''.join(map(str, self.request.user.groups.all())) == 'manager':
            print('permission access')
            return ModeratedProductForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            if self.object.user == self.request.user:
                context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
                context_data['form'] = ProductForm(data=self.request.POST, instance=self.object)
            elif ''.join(map(str, self.request.user.groups.all())) == 'manager':
                context_data['form'] = ModeratedProductForm
            else:
                context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
                context_data['form'] = ProductForm(data=self.request.POST, instance=self.object)
        else:
            if self.object.user == self.request.user:
                context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
                context_data['form'] = ProductForm(data=self.request.POST, instance=self.object)
            elif ''.join(map(str, self.request.user.groups.all())) == 'manager':
                context_data['form'] = ModeratedProductForm
            else:
                context_data['formset'] = ProductFormset(instance=self.object)
                context_data['form'] = ProductForm(instance=self.object)
        context_data['title'] = 'edit product'
        return context_data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()
            print("Formset data:", formset.data)
            if formset.is_valid():
                print("Formset is valid")
                formset.instance = self.object
                formset.save()
            else:
                print("Formset is not valid")
                print(formset.errors)
        return super().form_valid(form)


class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'
    success_url = reverse_lazy('catalog:catalog')


def show_category(request):
    category = request.GET.get('category')
    products = Product.objects.filter(category=category)
    category_name = Category.objects.get(pk=category).name
    context = {
        'title': 'catalog',
        'category_name': category_name,
        'is_filter_data': True,
        'products': products
    }
    return render(request, 'catalog/product_list.html', context)


def show_my_products(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'title': 'my products',
        'is_filter_data': True,
        'products': products,
    }
    return render(request, 'catalog/product_list.html', context)
