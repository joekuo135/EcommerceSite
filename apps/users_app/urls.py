from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^show_map$', views.show_map),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^login_user$', views.login_user),
    url(r'^create_user$', views.create_user),
    url(r'^user_profile$', views.user_profile),
    url(r'^logout$', views.logout),
    
    # url(r'^dashboard$', views.dashboard),

    # url(r'^logoff$', views.logout),
    # url(r'^register/create$', views.create_user),
    # url(r'^users/new/add$', views.admin_create_user),
    # url(r'^users/edit/(?P<user_id>\d+)/update_user$', views.update_user),
    # url(r'^users/edit/(?P<user_id>\d+)/update_password$', views.update_password),

]