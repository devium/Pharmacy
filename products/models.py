# -*- coding: utf-8 -*-


from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)
    featured = models.BooleanField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    side_effects = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=100, default=29.99)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)
    update_defaults = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'slug')

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

