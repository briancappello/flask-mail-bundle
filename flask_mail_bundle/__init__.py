"""
    flask_mail_bundle
    ~~~~~~~~~~~~~~~~~

    Adds email sending support to Flask Unchained

    :copyright: Copyright © 2018 Brian Cappello
    :license: MIT, see LICENSE for more details
"""

__version__ = '0.1.0'


from flask_unchained import Bundle

from .extensions import Mail, mail


class FlaskMailBundle(Bundle):
    command_group_names = ['mail']
