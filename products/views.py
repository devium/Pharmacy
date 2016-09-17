from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from products.models import Category, Product


def help(request):
    return render(request, 'help.html', {})


def delivery_help(request):
    return render(request, 'delivery_help.html', {})


def order_help(request):
    return render(request, 'order_help.html', {})


class HomePageView(TemplateView):
    template_name = 'index.html'


class CatalogueView(TemplateView):
    template_name = 'catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if kwargs['slug']:
            category = get_object_or_404(Category, slug=kwargs['slug'])
            context['products'] = category.products.all()
        else:
            context['products'] = Product.objects.all()
        return context


# TODO переместить в carts
class AddProductView(View):
    def get(self, request, pk, slug, *args, **kwargs):
        messages.success(request, 'Added')
        return redirect('catalogue', slug=slug)
