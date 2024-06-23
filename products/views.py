from django.views.generic import (
    CreateView, ListView, TemplateView, DeleteView
)
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Product
from products.forms import ProductForm


class HomeView(TemplateView):
    template_name = 'products/home.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/register.html'
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        self.object = form.save()
        messages.success(
            self.request, 'Product registered successfully!'
        )
        return super().form_valid(form)


class ProductListView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = super().get_queryset().order_by('value')
        products = list(map(self.format_value, products))
        return products
    
    def format_value(self, product):
        product.formatted_value = (
            f"R$ {product.value:,.2f}"
            .replace('.', 'X')
            .replace(',', '.')
            .replace('X', ',')
        )
        return product


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/list.html'
    success_url = reverse_lazy('products:list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().delete(request, *args, **kwargs)