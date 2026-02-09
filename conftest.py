import os
import django

def pytest_configure():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
    django.setup()