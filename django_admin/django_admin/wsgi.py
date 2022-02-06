import os
import sys
import platform
#путь к проекту, там где manage.py
sys.path.insert(0, '/home/f/fntlabyand/bot_fntlab_ru/public_html')

#путь к фреймворку, там где settings.py
sys.path.insert(0, '/home/f/fntlabyand/bot_fntlab_ru/public_html/django_admin/django_admin')

#путь к виртуальному окружению myenv
sys.path.insert(0, '/home/f/fntlabyand/bot_fntlab_ru/botenv/lib/python3.8/site-packages')


os.environ["DJANGO_SETTINGS_MODULE"] = "django_admin.django_admin.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()