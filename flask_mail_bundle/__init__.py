from flask_unchained import Bundle

from .extensions import Mail, mail


class FlaskMailBundle(Bundle):
    command_group_names = ['mail']
