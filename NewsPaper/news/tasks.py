from celery import shared_task
import time

from django.core.mail import send_mail


@shared_task()
def hello():
    time.sleep(10)
    print("Hello World!!!")


@shared_task()
def printer():
    send_mail(
        subject=f"Новости за неделю",
        message=f"Здравствуй."
                f" Новые новости в твоём любимом разделе! ",
        from_email='',
        recipient_list=['']
    )

