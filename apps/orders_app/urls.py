from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_item/(?P<product_id>\d+)$', views.add_item),
    url(r'^remove_item/(?P<product_id>\d+)$', views.remove_item),
    url(r'^create_cart/$', views.create_cart),
    ]