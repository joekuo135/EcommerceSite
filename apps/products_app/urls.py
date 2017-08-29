from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^create_item$', views.create_item),
    url(r'^show_dashboard$', views.show_dashboard),
    url(r'^show_product/(?P<product_id>\d+)$', views.show_product),
    ]