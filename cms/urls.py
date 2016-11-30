from django.conf.urls import url
from cms import views

urlpatterns = [
	url(r'^domain/$', views.domain_list, name='domain_list'),
	url(r'^domain/add/$', views.domain_edit, name='domain_add'),
	url(r'^domain/mod/(?P<domain_id>\d+)/$', views.domain_edit, name='domain_mod'),
	url(r'^domain/del/(?P<domain_id>\d+)/$', views.domain_del, name='domain_del'),
	url(r'^domain/add/file$', views.domain_add_byfile, name='domain_add_byfile'),
	url(r'^param/add/$', views.param_edit, name='param_add'),
	url(r'^param/mod/(?P<param_id>\d+)/$', views.param_edit, name='param_mod'),
	url(r'^param/del/(?P<param_id>\d+)/$', views.param_del, name='param_del'),
]
