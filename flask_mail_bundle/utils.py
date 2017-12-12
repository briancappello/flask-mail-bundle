import re

from flask_mail import Message

try:
    import lxml
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None


def get_message_plain_text(msg: Message):
    if msg.body:
        return msg.body

    if BeautifulSoup is None:
        from warnings import warn
        warn('WARNING: BeautifulSoup and/or lxml was not installed. Could not convert html message to plain text.')
        return msg.html

    plain_text = '\n'.join(map(
        str.strip,
        BeautifulSoup(msg.html, 'lxml').text.splitlines()
    ))
    return re.sub(r'\n\n', '\n\n', plain_text).strip()
