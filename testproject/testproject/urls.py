from django.conf.urls import patterns, include, url
from testing.views import HelloTemplate

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home/', 'testing.views.home', name='home'),
    url(r'^home1/', HelloTemplate.as_view()),
    url(r'^login/', 'testing.views.login', name='login'),
    url(r'^auth/$', 'testing.views.auth_view', name='auth'),
    url(r'^logout/', 'testing.views.logout', name='logout'),
    url(r'^invalid_login/','testing.views.invalid_login',name='invalid'),
    url(r'^loggedin/', 'testing.views.loggedin', name='loggedin'),
    url(r'^registration/$','testing.views.registration', name='reg'),
    url(r'^success/$','testing.views.success', name='success'),
    url(r'^form/$','testing.views.create', name='create'),
    #url(r'^ajax/$','testing.views.ajax', name='ajax'),


    url(r'^admin/', include(admin.site.urls)),
)
