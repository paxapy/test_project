from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView

from accounts.models import Profile
from accounts.forms import ProfileForm


class ProfileMixin(object):
    model = Profile
    success_url = '/'
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user


class AuthenticationMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AuthenticationMixin, self).dispatch(*args, **kwargs)


class ProfileDetailView(ProfileMixin, AuthenticationMixin, DetailView):
    pass


class ProfileUpdateView(ProfileMixin, AuthenticationMixin, UpdateView):
    pass
