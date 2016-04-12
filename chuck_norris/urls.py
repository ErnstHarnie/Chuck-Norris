from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^joke$', views.joke, name='joke')
	#url(r'^$', views.joke, name='joke'),
    #url(r'^(?P<character_id>[0-9]+)/$', views.character, name='character'),
]
