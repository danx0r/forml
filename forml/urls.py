from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'forml.views.home', name='home'),
)
