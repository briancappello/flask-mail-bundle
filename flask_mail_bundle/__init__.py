from flask_application_factory import Bundle

from .extension import mail
from .send_mail import send_mail, send_mail_async


class FlaskMailBundle(Bundle):
    module_name = __name__
    name = 'mail'
    extensions_module_name = 'extension'
