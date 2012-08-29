from django.views.generic.detail import DetailView
from models import Profile

class ProfileDetailView(DetailView):
    model = Profile

    def get_object(self, queryset=None):
        return self.request.user.profile