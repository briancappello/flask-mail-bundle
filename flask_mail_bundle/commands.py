import click

from flask.cli import with_appcontext

from .send_mail import send_mail, send_mail_async


TEST_EMAIL_TEMPLATE = 'flask_mail_bundle/email/__test_email__.html'


@click.group()
def mail():
    """Mail commands"""


@mail.command()
@click.argument('subject')
@click.argument('recipient')
@with_appcontext
def send_test_email(subject, recipient):
    send_mail(subject, recipient, TEST_EMAIL_TEMPLATE)


@mail.command()
@click.argument('subject')
@click.argument('recipient')
@with_appcontext
def send_test_async_email(subject, recipient):
    send_mail_async(subject, recipient, TEST_EMAIL_TEMPLATE)
