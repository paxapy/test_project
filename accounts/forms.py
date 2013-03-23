from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from accounts.models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('contacts', 'biography', 'birthday', 'last_name', 'first_name')
        widgets = {'birthday': AdminDateWidget()}
