# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    order = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order', )

    def get_url(self):
        return reverse("catalogue", kwargs={"slug": self.slug})


class Product(models.Model):
    title = models.CharField(max_length=120, unique=True)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    side_effects = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True, related_name='products')
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    update_defaults = models.BooleanField(default=False)
    count = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def get_price(self):
        return self.price

    def get_absolute_url(self):
        return reverse("single_product", kwargs={"slug": self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


class Order(models.Model):
    date = models.DateField(auto_now_add=True)
    processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return str(self.pk)


class SelectedProduct(models.Model):
    user = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    order = models.ForeignKey(Order)

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return self.product.title
