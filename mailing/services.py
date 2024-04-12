from mailing.models import Mailing


def send_mailing(mailing):
    pass


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
