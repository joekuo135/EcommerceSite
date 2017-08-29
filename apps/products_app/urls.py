from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^populate_database$', views.populate_database),
    url(r'^show_dashboard/(?P<category>Mens|Womens|Accessories)$', views.show_dashboard),
    url(r'^show_product/(?P<product_id>\d+)$', views.show_product),
    ]