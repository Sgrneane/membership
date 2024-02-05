from django.conf import settings
from django.core.mail import send_mail
email_from = settings.EMAIL_HOST_USER
from django.core.mail import EmailMessage
import asyncio
import time
import threading

def NotifyUsers(instance):
    message = ''  # Your HTML content goes here
    recipient_list = instance.groups.all().values_list('users__email', flat=True)

    plain_message = instance.description
    subject = instance.subject
    recipient_list = list(set(recipient_list))

    email = EmailMessage(subject, plain_message, email_from, [], recipient_list, headers={'Message-ID': 'foo'})
    email.content_subtype = "html"  # Set the content type to HTML
    # await asyncio.sleep(10)
    email.send()
    return True


def NotifyEvent(instance):
    message = ''  # Your HTML content goes here
    recipient_list = instance.groups.all().values_list('users__email',flat=True)

    plain_message = instance.description
    subject = instance.name
    recipient_list = list(set(recipient_list))

    email = EmailMessage(subject, plain_message, email_from, [], recipient_list, headers={'Message-ID': 'foo'})
    email.content_subtype = "html"  # Set the content type to HTML
    # await asyncio.sleep(10)
    email.send()
    return True

def ThreadedNotification(instance,model):
    if model == 'Notifications':
        t1 = threading.Thread(
            target=NotifyUsers,
            args=(instance,)
        )
        t1.start()
    elif model == 'Event':
        t1 = threading.Thread(
            target=NotifyEvent,
            args=(instance,)
        )
        t1.start()