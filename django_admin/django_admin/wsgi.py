import os
import sys

# project root path for deployment in production
# sys.path.insert(0, 'path/to/project/root')

# python site-packages virtual env path for deployment in production
# sys.path.insert(0, 'path/to/site-packages')


os.environ["DJANGO_SETTINGS_MODULE"] = "django_admin.django_admin.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()