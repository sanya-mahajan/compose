"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""
import os
import pathlib
import dotenv
import sys
from django.core.wsgi import get_wsgi_application
CURRENT_DIR=pathlib.Path(__file__).resolve().parent
BASE_DIR = CURRENT_DIR.parent
ENV_FILE_PATH=BASE_DIR / ".env"
print("---===-----===-----",CURRENT_DIR)
dotenv.read_dotenv(str(ENV_FILE_PATH))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()