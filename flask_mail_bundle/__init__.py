from flask_unchained import Bundle

from .extensions import mail
from .send_mail import send_mail, send_mail_async


class FlaskMailBundle(Bundle):
    command_group_names = ['mail']
