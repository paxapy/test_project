from django.conf import settings

def context_settings(request):
    return {'settings': settings, 'ADMIN_MEDIA_PREFIX':settings.ADMIN_MEDIA_PREFIX}