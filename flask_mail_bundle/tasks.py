from .extensions import mail
from .utils import get_message_plain_text

try:
    from flask_celery_bundle import celery
except ImportError:
    class celery:
        @staticmethod
        def task(*args, **kwargs):
            return lambda fn: None


@celery.task(serializer='pickle')
def send_mail_async_task(msg):
    msg.body = get_message_plain_text(msg)
    mail.send(msg)
