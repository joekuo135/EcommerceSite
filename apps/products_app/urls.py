from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show$', views.show),
    url(r'^create_item$', views.create_item),
    url(r'^show_dashboard$', views.show_dashboard),


    ]