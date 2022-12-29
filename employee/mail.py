from django.core.mail import send_mail
import smtplib
import os


def send(SUBJECT, TEXT):
    send_mail(
        SUBJECT, TEXT,
        'iNewton@gmail.com',
        ['ifeanyi.okala.247238@unn.edu.ng'],
        fail_silently=False,
    )
