from django.shortcuts import render
from django.views.generic import TemplateView


def home(request):
    return render(request, 'index.html', {})


def catalogue(request):
    return render(request, 'catalogue.html', {})


def help(request):
    return render(request, 'help.html', {})


def delivery_help(request):
    return render(request, 'delivery_help.html', {})


def order_help(request):
    return render(request, 'order_help.html', {})


class HomePageView(TemplateView):
    template_name = 'index.html'
