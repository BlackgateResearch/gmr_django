import os
import sys

path = '/usr/share/gmr/unstable/'
if path not in sys.path:
    sys.path.append(path)

project_path = '/usr/share/gmr/unstable/gmr_django/'
if project_path not in sys.path:
    sys.path.append(project_path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gmr_django.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
