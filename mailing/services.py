from smtplib import SMTPException

from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings

from mailing.models import Mailing, Log


def daily_tasks():
    mailings = Mailing.objects.filter(request_period="Ежедневно", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def weekly_tasks():
    mailings = Mailing.objects.filter(request_period="Еженедельно", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def monthly_tasks():
    mailings = Mailing.objects.filter(request_period="Ежемесячно", status="Запущена")
    if mailings.exists():
        for mailing in mailings:
            send_mailing(mailing)


def send_mailing():
    now = timezone.localtime(timezone.now())
    mailing_list = Mailing.objects.all()
    for mailing in mailing_list:
        if mailing.end_time < now:
            mailing.status = Mailing.COMPLETED
            continue
        if mailing.starte_time <= now < mailing.end_time:
            mailing.status = Mailing.STARTED
            mailing.save()

            for client in mailing.clients.all():
                try:
                    send_mail(
                        subject=mailing.massage.subject,
                        message=mailing.massage.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email],
                    )

                    log = Log.objects.create(
                        mailing=mailing,
                        last_try=mailing.start_time,
                        status=True,
                        mail_service_responce='Ok',
                    )
                    log.save()

                    return log

                except SMTPException as error:
                    log = Log.objects.create(
                        mailling=mailing,
                        last_try=mailing.start_time,
                        status=False,
                        mail_service_responce=error
                    )
                    log.save()

                    return log

        else:
            mailing.status = Mailing.COMPLETED
            mailing.save()
