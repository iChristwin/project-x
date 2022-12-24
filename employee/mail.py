import smtplib
import os


PSWD = os.environ.get("VAR1")


def send(SUBJECT, TEXT):
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("nsukkaai@gmail.com", "itisworthmylifetime")

    # message to be sent
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    # sending the mail
    s.sendmail("nsukkaai@gmail.com", "info@learnhall.com", message)

    # terminating the session
    s.quit()


