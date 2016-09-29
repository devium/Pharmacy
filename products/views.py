from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from products.models import Category, Product, SelectedProduct, Order


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
        cart = self.request.session.get('cart', {})
        items = []
        summa = 0
        for item in Product.objects.filter(pk__in=cart.keys()):
            item.quantity = cart.get(str(item.pk), 0)
            summa += item.quantity * item.sale_price if item.sale_price else item.quantity * item.price
            items.append(item)
        context['items'] = items
        context['summa'] = summa
        return context


@never_cache
def logout_view(request):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    logout(request)
    return redirect('home')


class HistoryView(LoginRequiredMixin, TemplateView):
    template_name = 'history.html'
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = SelectedProduct.objects.filter(user=self.request.user)
        return context


class BuyView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        cart = request.session.get('cart', {})
        o = Order.objects.create()
        items_info = []
        for i, q in cart.items():
            pr = get_object_or_404(Product, pk=int(i))
            SelectedProduct.objects.create(user=self.request.user, quantity=q, product=pr, order=o)
            item_info = "{} x{}".format(pr.title, q)
            items_info.append(item_info)

        current_site = get_current_site(request)
        site_name = current_site.name
        send_mail(
            'Order',
            '\n'.join(items_info),
            'order@{}'.format(site_name),
            [request.user.email],
        )
        messages.success(request, 'Done')
        return redirect('home')

