from django.conf.urls import patterns, include, url

from report.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sikshana_report.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',main),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$',about)
)
