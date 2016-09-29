from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve

from products.views import HomePageView, CatalogueView, AddProductView, CartView, RemoveCartView, AddCartView, \
    logout_view, HistoryView, BuyView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/profile/$', HistoryView.as_view(), name='history'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^add/(?P<pk>.*)/(?P<slug>.*)$', AddProductView.as_view(), name='add_product'),
    url(r'^plus/(?P<pk>.*)/$', AddCartView.as_view(), name='add_cart'),
    url(r'^remove/(?P<pk>.*)/$', RemoveCartView.as_view(), name='remove_cart'),
    url(r'^catalogue/(?P<slug>.*)/$', CatalogueView.as_view(), name='catalogue'),
    url(r'^help/$', TemplateView.as_view(template_name='help.html'), name='help'),
    url(r'^buy/$', BuyView.as_view(), name='buy'),
    url(r'^cart/$', CartView.as_view(), name='cart'),
    # url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]

if settings.DEBUG:
    # media files (images, css, javascript, etc.)
    urlpatterns += [url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})]
