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

class DbNote(models.Model):
    CHOICES =(
        ('c', 'created'),
        ('u', 'updated'),
        ('d', 'deleted')
    )
    note = models.CharField(choices=CHOICES, max_length=1)
    model = models.CharField(max_length=142)
    timestamp = models.DateTimeField(auto_now_add=True)

def create_profile(**kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])

def del_note(sender, **kwargs):
    DbNote.objects.create(note='d',model=sender.__name__)

def save_note(sender, **kwargs):
    if kwargs['created']:
        if sender.__name__ != 'DbNote':
            DbNote.objects.create(note='c',model=sender.__name__)
    else:
        DbNote.objects.create(note='u',model=sender.__name__)

models.signals.post_save.connect(create_profile, sender=User)
models.signals.post_save.connect(save_note)
models.signals.post_delete.connect(del_note)