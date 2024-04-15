from datetime import datetime, timedelta
from smtplib import SMTPException

from django.conf import settings
from django.core.cache import cache
from django.core.mail import send_mail
from django.utils import timezone

from mailing.models import Log, Mailing


def daily_tasks():
    now = timezone.localtime(timezone.now())
    mailings = Mailing.objects.filter(request_period="Ежедневно")
    if mailings.exists():
        for mailing in mailings:
            if mailing.start_time <= now < mailing.end_time:
                if (
                    mailing.status == "Создана"
                    or datetime.now().date() >= mailing.next_mailing
                ):
                    send_mailing(mailing)
                else:
                    continue
            else:
                continue


def weekly_tasks():
    now = timezone.localtime(timezone.now())
    mailings = Mailing.objects.filter(request_period="Еженедельно")
    if mailings.exists():
        for mailing in mailings:
            if mailing.start_time <= now < mailing.end_time:
                if (
                    mailing.status == "Создана"
                    or datetime.now().date() >= mailing.next_mailing
                ):
                    send_mailing(mailing)
                else:
                    continue
            else:
                continue


def monthly_tasks():
    now = timezone.localtime(timezone.now())
    mailings = Mailing.objects.filter(request_period="Ежемесячно")
    if mailings.exists():
        for mailing in mailings:
            if mailing.start_time <= now < mailing.end_time:
                if (
                    mailing.status == "Создана"
                    or datetime.now().date() >= mailing.next_mailing
                ):
                    send_mailing(mailing)
                else:
                    continue
            else:
                continue


def send_mailing(mailing):
    day = timedelta(days=1)
    weak = timedelta(days=7)
    month = timedelta(days=30)

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
                last_try=datetime.now(),
                status=True,
                mail_service_responce="Ok",
            )
            log.save()

            mailing.status = Mailing.COMPLETED
            mailing.last_mailing = datetime.now().date()
            if mailing.request_period == "Ежедневно":
                mailing.next_mailing = mailing.last_mailing + day
            elif mailing.request_period == "Еженедельно":
                mailing.next_mailing = mailing.last_mailing + weak
            elif mailing.request_period == "Ежемесячно":
                mailing.next_mailing = mailing.last_mailing + month
            mailing.save()
            return log

        except SMTPException as error:
            log = Log.objects.create(
                mailling=mailing,
                last_try=datetime.now(),
                status=False,
                mail_service_responce=error,
            )
            log.save()

            mailing.status = Mailing.COMPLETED
            mailing.save()
            return log


def get_cache_for_mailings():
    if settings.CACHE_ENABLED:
        key = "mailings_count"
        mailings_count = cache.get(key)
        if mailings_count is None:
            mailings_count = Mailing.objects.all().count()
            cache.set(key, mailings_count)
    else:
        mailings_count = Mailing.objects.all().count()
    return mailings_count
