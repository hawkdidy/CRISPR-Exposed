"""
WSGI config for crispr_exposed project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crispr_exposed.settings_prod") #crispr_exposed.settings_prod

application = get_wsgi_application()
