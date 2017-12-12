from flask_application_factory import Bundle

from .extension import mail
from .send_mail import send_mail, send_mail_async


class FlaskMailBundle(Bundle):
    module_name = __name__
    command_group_names = ['mail']
    extensions_module_name = 'extension'
