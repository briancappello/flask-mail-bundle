import os

from flask_unchained.utils import get_boolean_env


class BaseConfig:
    MAIL_SERVER = os.getenv('FLASK_MAIL_HOST', 'localhost')
    MAIL_PORT = os.getenv('FLASK_MAIL_PORT', 25)
    MAIL_USE_TLS = get_boolean_env('FLASK_MAIL_USE_TLS', False)
    MAIL_USE_SSL = get_boolean_env('FLASK_MAIL_USE_SSL', False)
    MAIL_USERNAME = os.getenv('FLASK_MAIL_USERNAME', None)
    MAIL_PASSWORD = os.getenv('FLASK_MAIL_PASSWORD', None)
    MAIL_DEFAULT_SENDER = (
        os.getenv('FLASK_MAIL_DEFAULT_SENDER_NAME', 'Flask Mail'),
        os.getenv('FLASK_MAIL_DEFAULT_SENDER_EMAIL',
                  f"noreply@{os.getenv('FLASK_DOMAIN', 'localhost')}")
    )


class DevConfig(BaseConfig):
    MAIL_PORT = os.getenv('FLASK_MAIL_PORT', 1025)  # MailHog


class ProdConfig(BaseConfig):
    MAIL_PORT = os.getenv('FLASK_MAIL_PORT', 465)
    MAIL_USE_SSL = get_boolean_env('FLASK_MAIL_USE_SSL', True)


class StagingConfig(ProdConfig):
    pass


class TestConfig(BaseConfig):
    pass
