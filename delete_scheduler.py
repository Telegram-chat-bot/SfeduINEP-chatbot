import schedule
from datetime import datetime, timedelta
import time


def setup_django():
    import os
    import django
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_admin.django_admin.settings'
    django.setup()


setup_django()


def delete_task():
    from django_admin.feedback.models import Feedback
    Feedback.objects.filter(date__lte=datetime.now() - timedelta(days=30)).delete()


schedule.every().day.at("07:00").do(delete_task)
while True:
    schedule.run_pending()
    time.sleep(1)
