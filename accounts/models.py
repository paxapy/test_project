from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    birthday = models.DateField(null=True)
    biography = models.TextField()
    contacts = models.TextField()


class DbNote(models.Model):

    CREATED = 'c'
    UPDATED = 'u'
    DELETED = 'd'
    CHOICES = (
        (CREATED, 'created'),
        (UPDATED, 'updated'),
        (DELETED, 'deleted')
    )
    note = models.CharField(choices=CHOICES, max_length=1)
    model = models.CharField(max_length=142)
    timestamp = models.DateTimeField(auto_now_add=True)


def del_note(sender, **kwargs):
    DbNote.objects.create(note=DbNote.DELETED, model=sender.__name__)


def save_note(sender, **kwargs):
    if kwargs.get('created'):
        if sender.__name__ != 'DbNote':
            DbNote.objects.create(note=DbNote.CREATED, model=sender.__name__)
    else:
        DbNote.objects.create(note=DbNote.UPDATED, model=sender.__name__)


models.signals.post_save.connect(save_note)
models.signals.post_delete.connect(del_note)
