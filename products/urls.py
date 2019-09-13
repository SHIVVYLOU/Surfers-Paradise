from django.conf.urls import url
from .views import get_products, product_detail, create_or_edit_product

urlpatterns = [
    url(r'^$', get_products, name='get_products'),
    url(r'^(?P<pk>\d+)/$', product_detail, name='product_detail'),
    url(r'^new/$', create_or_edit_product, name='new_product'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_product, name='edit_product')
]