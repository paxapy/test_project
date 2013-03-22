from django.db import models
from django.core.management.base import NoArgsCommand


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        print('Objects counts - Model: count')
        for model in models.get_models():
            print(
                '{0}: {1}'.format(
                    model.__name__,
                    model.objects.count(),
                )
            )
