# Flask Mail Bundle

Adds email sending support to Flask Unchained

# Install

Install from PyPI:

```bash
$ pip install flask_mail_bundle
```

And add it to your `unchained_config.BUNDLES`:

```python
# your_app_package/unchained_config.py

BUNDLES = [
    'flask_mail_bundle',
    # ...
]
```

# Configure

The default configuration will send mails to [MailHog](https://github.com/mailhog/MailHog) in development (`127.0.0.1:1025`), and to your system MTA over SSL in production/staging (`127.0.0.1:465`).

Stock Flask-Mail configuration options:

Config Name | Default Env Var Name | Default Value | Description
----------- | -------------------- | ------------- | -----------
MAIL_SERVER | FLASK_MAIL_SERVER | 127.0.0.1 | IP or domain of the MTA host
MAIL_PORT | FLASK_MAIL_PORT | DEV: 1025 PROD/STAGING: 465 | Port of the MTA
MAIL_USERNAME | FLASK_MAIL_USERNAME | None | MTA username
MAIL_PASSWORD | FLASK_MAIL_PASSWORD | None | MTA password
MAIL_USE_TLS | FLASK_MAIL_USE_TLS | False | Whether or not to send using TLS
MAIL_USE_SSL | FLASK_MAIL_USE_SSL | DEV: False PROD/STAGING: True | Whether or not to send using SSL
MAIL_DEFAULT_SENDER | FLASK_MAIL_DEFAULT_SENDER | `Flask Mail <noreply@localhost>` | The default sender
MAIL_DEBUG | FLASK_MAIL_DEBUG | int(current_app.debug) | The debug level for Flask-Mail
MAIL_MAX_EMAILS | FLASK_MAIL_MAX_EMAILS | None | Max number of emails per connection to the MTA
MAIL_SUPPRESS_SEND | FLASK_MAIL_SUPPRESS_SEND | bool(current_app.testing) | Whether or not to suppress actually sending to the MTA
MAIL_ASCII_ATTACHMENTS | FLASK_MAIL_ASCII_ATTACHMENTS | False | Whether or not to convert attachment filenames encoded in UTF-8 to ASCII
MAIL_SEND_FN | n/a | flask_mail_bundle.utils._send_mail |

## Customizing the MAIL_SEND_FN

You can also customize the function used to send emails by setting `MAIL_SEND_FN`. It must have the same signature as the default. For example, if you wanted to send a list of emails using the same connection to the MTA, you might do something like this:

```python
from flask_mail import Message
from flask_mail_bundle import mail
from flask_mail_bundle.utils import _send_mail

def bulk_send_mail(subject_or_message, to=None, template=None, **kwargs):
    if (isinstance(subject_or_message, (list, tuple))
            and len(subject_or_message)
            and isinstance(subject_or_message[0], Message)):
        with mail.connect() as connection:
            for msg in subject_or_message:
                connection.send(msg)
    else:
        _send_mail(subject_or_message, to, template, **kwargs)


# and in your app bundle config:
class BaseConfig:
    # ...
    MAIL_SEND_FN = bulk_send_mail
```
