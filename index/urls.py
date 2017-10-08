from django.conf.urls import url
from . import views

app_name = "index"

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    #portfolio/pk   - uses a named group which usually takes the format: '?<name>pattern'
    url(r'^portfolio/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'^blog/$', views.BlogView.as_view(), name='blog'),

]
