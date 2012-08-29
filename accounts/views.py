from django.views.generic.detail import DetailView

from models import Profile
from factories import ProfileFactory

class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self, queryset=None):
        return ProfileFactory.stub()