import logging
from datetime import datetime, timedelta


async def delete_old_feedback():
    from django_admin.feedback.models import Feedback
    import pytz
    computed_time = datetime.now() - timedelta(days=60)
    moscow_timezone = pytz.timezone('Europe/Moscow')

    date_search = moscow_timezone.localize(computed_time)
    Feedback.objects.filter(created_at__lt=date_search).delete()
    logging.info("Scheduler is running")
