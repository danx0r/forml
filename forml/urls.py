from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^form1$', 'forml.views.form1'),
    url(r'^form2$', 'forml.views.form2'),
)
