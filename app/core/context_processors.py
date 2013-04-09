from django.conf import settings


def settings_processor(request):
    return {'PROJECT_SETTINGS': settings}