import os
import sys

path = '/usr/share/gmr/unstable/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gmr_django.settings'

import gmr_django.django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
