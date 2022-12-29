from django.test import TestCase
from django.core.mail import send_mail


def send_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'iNewton@gmail.com',
        ['ifeanyi.okala.247238@unn.edu.ng'],
        fail_silently=False,
    )
