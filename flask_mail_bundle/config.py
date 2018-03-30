import os

from flask import current_app
from flask_unchained.utils import get_boolean_env
from werkzeug.local import LocalProxy

from .utils import send_mail


class BaseConfig:
    MAIL_SERVER = os.getenv('FLASK_MAIL_HOST', '127.0.0.1')
    MAIL_USERNAME = os.getenv('FLASK_MAIL_USERNAME', None)
    MAIL_PASSWORD = os.getenv('FLASK_MAIL_PASSWORD', None)
    MAIL_PORT = os.getenv('FLASK_MAIL_PORT', 25)
    MAIL_USE_TLS = get_boolean_env('FLASK_MAIL_USE_TLS', False)
    MAIL_USE_SSL = get_boolean_env('FLASK_MAIL_USE_SSL', False)
    MAIL_DEFAULT_SENDER = (
        os.getenv('FLASK_MAIL_DEFAULT_SENDER_NAME', 'Flask Mail'),
        os.getenv('FLASK_MAIL_DEFAULT_SENDER_EMAIL',
                  f"noreply@{os.getenv('FLASK_DOMAIN', 'localhost')}"))
    MAIL_SEND_TASK = send_mail

    MAIL_DEBUG = LocalProxy(
        lambda: int(os.getenv('FLASK_MAIL_DEBUG', current_app.debug)))
    MAIL_MAX_EMAILS = os.getenv('FLASK_MAIL_MAX_EMAILS', None)
    MAIL_SUPPRESS_SEND = LocalProxy(
        lambda: os.getenv('FLASK_MAIL_SUPPRESS_SEND', current_app.testing))
    MAIL_ASCII_ATTACHMENTS = os.getenv('FLASK_MAIL_ASCII_ATTACHMENTS', False)


class DevConfig(BaseConfig):
    MAIL_PORT = os.getenv('FLASK_MAIL_PORT', 1025)  # MailHog


class ProdConfig(BaseConfig):
    MAIL_PORT = os.getenv('FLASK_MAIL_PORT', 465)
    MAIL_USE_SSL = get_boolean_env('FLASK_MAIL_USE_SSL', True)


class StagingConfig(ProdConfig):
    pass


class TestConfig(BaseConfig):
    TESTING = True
