from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^pyas2/', include('pyas2.urls')),
    url(r'^admin/', include(admin.site.urls)),
)