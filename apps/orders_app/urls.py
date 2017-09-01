from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^update_cart/(?P<product_id>\d+)$', views.update_cart),

    ]