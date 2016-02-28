from django.shortcuts import render


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