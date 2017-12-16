from flask_unchained import Bundle

from .extension import mail
from .send_mail import send_mail, send_mail_async


class FlaskMailBundle(Bundle):
    name = 'mail'
    extensions_module_name = 'extension'
