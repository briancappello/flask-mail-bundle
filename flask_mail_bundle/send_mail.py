from flask import current_app as app, render_template
from flask_mail import Message

from .extensions import mail
from .tasks import send_mail_async_task
from .utils import get_message_plain_text


def _get_message(subject, recipients, template, sender, **ctx):
    if not isinstance(recipients, (tuple, list)):
        recipients = [recipients]
    msg = Message(subject=subject, recipients=recipients, sender=sender)
    msg.html = render_template(template, **ctx)
    return msg


def send_mail(subject, recipients, template, sender=None, **ctx):
    msg = _get_message(subject, recipients, template, sender, **ctx)
    msg.body = get_message_plain_text(msg)
    mail.send(msg)


def send_mail_async(subject, recipients, template, sender=None, **ctx):
    if send_mail_async_task is None:
        from warnings import warn
        warn('ERROR: flask-celery-bundle is not installed. Falling back to '
             'synchronous send.')
        return send_mail(subject, recipients, template, sender, **ctx)

    msg = _get_message(subject, recipients, template, sender, **ctx)

    if app and app.config.get('TESTING'):
        return send_mail_async_task.apply([msg])
    return send_mail_async_task.delay(msg)
