from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.views import login, logout

from accounts.views import ProfileDetailView, ProfileUpdateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_project.views.home', name='home'),
    # url(r'^test_project/', include('test_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProfileDetailView.as_view(), name='profile_detail'),
    url(r'^accounts/login/$', login, {'template_name':'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page':'/'}, name='logout'),
    url(r'^profile/$', ProfileUpdateView.as_view(), name='profile_update')
)
