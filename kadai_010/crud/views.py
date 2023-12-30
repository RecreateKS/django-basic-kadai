from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product


class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
