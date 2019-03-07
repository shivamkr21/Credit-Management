from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$', views.index,name='index'),
	url(r'^member/',views.member,name='member'),
	url(r'^detail/',views.detail,name='detail'),
	url(r'^details/',views.details,name='details'),
	url(r'^transferfrom/',views.transferfrom,name='transferfrom'),
	url(r'^transferto/',views.transferto,name='transferto'),
	url(r'^trncrd/',views.trncrd,name='trncrd'),
	url(r'^transaction/',views.transaction,name='transaction'),
]
