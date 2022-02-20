from datetime import datetime, timedelta


def setup_django():
    import os
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_admin.settings'
    django.setup()


def delete_task():
    from django_admin.feedback.models import Feedback
    Feedback.objects.filter(date__lte=datetime.now() - timedelta(days=30)).delete()


setup_django()
delete_task()