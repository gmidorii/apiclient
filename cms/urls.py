from django.conf.urls import url
from cms import views

urlpatterns = [
	url(r'^domain/$', views.domain_list, name='domain_list')
	url(r'^domain/add/$', views.domain_edit, name='domain_add')
	url(r'^domain/mod/(?P<domain_id>\d+)/$', views.domain_edit, name='domain_mod')
	url(r'^domain/del/(?P<domain_id>\d+)/$', views.domain_del, name='domain_del')
]
