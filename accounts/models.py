from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=142)
    last_name = models.CharField(max_length=142)
    birthday = models.DateField(null=True)
    biography = models.TextField()
    contacts = models.TextField()

def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

models.signals.post_save.connect(create_profile, sender=User)