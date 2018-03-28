from flask import current_app as app
from flask_mail import Mail as BaseMail


class Mail(BaseMail):
    def init_app(self, app):
        self.state = super().init_app(app)
        app.extensions['mail'] = self

    def __getattr__(self, name):
        # overridden to allow for runtime-modified config values
        state_value = getattr(self.state, name, None)
        try:
            return app.config.get(('mail_' + name).upper(), state_value)
        except RuntimeError:
            raise AttributeError(name)
