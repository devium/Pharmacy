from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from products.views import HomePageView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'products.views.home', name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
    # url(r'^catalogue$', 'products.views.catalogue', name='catalogue'),
    # url(r'^help$', 'products.views.help', name='help'),
    # url(r'^delivery_help$', 'products.views.delivery_help', name='delivery_help'),
    # url(r'^order_help$', 'products.views.order_help', name='order_help'),
    # url(r'^cart$', 'carts.views.cart', name='cart'),
    # url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    # media files (images, css, javascript, etc.)
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
