"""
WSGI config for LEDjango project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
from gevent import monkey
import os
from django.core.wsgi import get_wsgi_application
import leancloud
from gevent.pywsgi import WSGIServer
from leancloud import Engine

monkey.patch_all()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LEDjango.settings")

engine = Engine(get_wsgi_application())

APP_ID = os.environ['LC_APP_ID']
MASTER_KEY = os.environ['LC_APP_MASTER_KEY']
PORT = int(os.environ['LC_APP_PORT'])

leancloud.init(APP_ID, master_key=MASTER_KEY)

application = engine

if __name__ == '__main__':
    server = WSGIServer(('localhost', PORT), application)
    server.serve_forever()
