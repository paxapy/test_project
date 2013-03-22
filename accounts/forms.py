from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from accounts.models import Profile


class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = Profile
        fields = ('contacts', 'biography', 'birthday', 'last_name', 'first_name')
