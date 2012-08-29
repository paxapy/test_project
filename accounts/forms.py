from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from models import Profile

class ProfileForm(forms.ModelForm):

    birthday = forms.DateField(widget=AdminDateWidget())

    class Meta:
        model = Profile
        exclude = ('user',)
