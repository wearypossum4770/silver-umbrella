# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from django import get_version

from .celery import app as celery_app

__all__ = ("celery_app",)


# git tag v1.2.3 -m "Release version 1.2.3"
# __version__ = (0, 0, 1, "alpha",0)
__author__ = ""
__email__ = ""
__url__ = ""
__license__ = ""
VERSION = (0, 0, 1, "alpha", 0)

__version__ = get_version(VERSION)
