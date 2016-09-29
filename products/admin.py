# -*- coding: utf-8 -*-


from django.contrib import admin

from .models import Product, ProductImage, Category, Order, SelectedProduct


class ProductAdmin(admin.ModelAdmin):
    # date_hierarchy = 'timestamp'
    # search_fields = ['title', 'description', 'ingredients', 'directions', 'side_effects']
    # list_display = ['title', 'price', 'active', 'updated']
    # list_editable = ['price', 'active']
    # list_filter = ['price', 'active']
    # readonly_fields = ['updated', 'timestamp']
    # prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('category',)

    class Meta:
        model = Product


class SelectedProductInline(admin.TabularInline):
    model = SelectedProduct
    exclude = ['user']


class OrderAdmin(admin.ModelAdmin):
    inlines = [SelectedProductInline]
    list_display = ['pk', 'processed']
    list_filter = ['processed']

    class Meta:
        model = Order

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
