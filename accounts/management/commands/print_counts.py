from django.db import models
from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        for model in models.get_models():
           print 'Model: {0}, objects: {1}'.format(model._meta.app_label,
               model.objects.all().count())
