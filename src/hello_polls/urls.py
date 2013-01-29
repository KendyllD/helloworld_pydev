from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from hello_polls.models import MyPoll


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloworld_pydev.views.home', name='home'),
    # url(r'^helloworld_pydev/', include('helloworld_pydev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$',
        ListView.as_view(
            queryset=MyPoll.objects.order_by('-pub_date')[:3],
            context_object_name='latest_mypoll_list',
            template_name='hello_polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=MyPoll,
            template_name='hello_polls/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=MyPoll,
            template_name='hello_polls/results.html'),
        name='mypoll_results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'hello_polls.views.vote'),
)