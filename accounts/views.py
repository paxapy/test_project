from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from models import Profile
from factories import ProfileFactory

class ProfileMixin(object):
    model = Profile
    success_url = '/'


class AuthenticationMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthenticationMixin, self).dispatch(*args, **kwargs)

class ProfileDetailView(ProfileMixin, DetailView):

    def get_object(self, queryset=None):
        return ProfileFactory.stub()

class ProfileUpdateView(ProfileMixin, AuthenticationMixin, UpdateView):

    def get_object(self, queryset=None):
        return self.request.user.profile