from flask_mail import Mail as BaseMail


class Mail(BaseMail):
    def init_app(self, app):
        self.app = app
        self.state = super().init_app(app)

    def __getattr__(self, name):
        # overridden to allow for runtime-changed config values
        state_value = getattr(self.state, name, None)
        return self.app.config.get(('mail_' + name).upper(), state_value)


mail = Mail()


EXTENSIONS = {
    'mail': mail,
}
