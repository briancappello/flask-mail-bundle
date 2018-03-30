from flask_unchained import Bundle

from .extensions import mail
from .utils import make_message


class FlaskMailBundle(Bundle):
    command_group_names = ['mail']
