from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve

from products.views import HomePageView, CatalogueView, AddProductView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^add/(?P<pk>.*)/(?P<slug>.*)$', AddProductView.as_view(), name='add_product'),
    url(r'^catalogue/(?P<slug>.*)$', CatalogueView.as_view(), name='catalogue'),
    url(r'^help$', TemplateView.as_view(template_name='help.html'), name='help'),
    # url(r'^delivery_help$', 'products.views.delivery_help', name='delivery_help'),
    # url(r'^order_help$', 'products.views.order_help', name='order_help'),
    # url(r'^cart$', 'carts.views.cart', name='cart'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    # media files (images, css, javascript, etc.)
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
