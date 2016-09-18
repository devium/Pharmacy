from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import resolve
from django.urls import reverse
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


class AddProductView(View):
    def get(self, request, pk, slug, *args, **kwargs):
        messages.success(request, 'Added')
        if 'cart' not in request.session:
            request.session['cart'] = {pk: 1}
        else:
            request.session['cart'][pk] = request.session['cart'].get(pk, 0) + 1
        return redirect('catalogue', slug=slug)


class AddCartView(View):
    def get(self, request, pk, *args, **kwargs):
        if 'cart' not in request.session:
            request.session['cart'] = {pk: 1}
        else:
            request.session['cart'][pk] = request.session['cart'].get(pk, 0) + 1
        return redirect('cart')


class RemoveCartView(View):
    def get(self, request, pk, *args, **kwargs):
        if 'cart' in request.session:
            count = request.session['cart'].pop(pk, 0)
            if count:
                request.session['cart'][pk] = count - 1
        return redirect('cart')


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart')
        items = []
        summa = 0
        for item in Product.objects.filter(pk__in=cart.keys()):
            item.quantity = cart.get(str(item.pk), 0)
            summa += item.quantity * item.sale_price if item.sale_price else item.quantity * item.price
            items.append(item)
        context['items'] = items
        context['summa'] = summa
        return context
