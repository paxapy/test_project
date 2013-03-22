from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

from accounts.views import ProfileDetailView, ProfileUpdateView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProfileDetailView.as_view(), name='profile_detail'),
    url(r'^accounts/login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/$', ProfileUpdateView.as_view(), name='profile_update')
)
