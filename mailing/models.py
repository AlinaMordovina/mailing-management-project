from django.db import models


class Client(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    middlename = models.CharField(max_length=100, verbose_name='Отчество', blank=True, null=True)
    email = models.EmailField(verbose_name='Почта', unique=True)
    comment = models.TextField(verbose_name='Комментарий', blank=True, null=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}: {self.email}'

    class Meta:
        verbose_name = 'Клиент сервиса'
        verbose_name_plural = 'Клиенты сервиса'
        ordering = ('lastname', 'firstname',)


class Mailing(models.Model):
    # добавить время последней рассылки? нужно для автоматического расписания
    DAILY = 'Ежедневно'
    WEEKLY = 'Еженедельно'
    MONTHLY = 'Ежемесячно'

    PERIOD_CHOICES = [
        (DAILY,  'Ежедневно'),
        (WEEKLY, 'Еженедельно'),
        (MONTHLY, 'Ежемесячно')
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (CREATED, 'Создана'),
        (STARTED, 'Запущена'),
        (COMPLETED, 'Завершена')
    ]

    start_time = models.TimeField(verbose_name='Время начала рассылки')
    end_time = models.TimeField(verbose_name='Время окончания рассылки')
    request_period = models.CharField(max_length=50, choices=PERIOD_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=CREATED, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True)

    clients = models.ManyToManyField(Client, verbose_name='Клиенты рассылки')

    def __str__(self):
        return f'{self.request_period} с {self.start_time} по {self.end_time}'

    class Meta:
        verbose_name = 'Почтовая рассылка'
        verbose_name_plural = 'Почтовые рассылки'


class Massage(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Почтовая рассылка')
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение для рассылки'
        verbose_name_plural = 'Сообщения для рассылок'


class Log(models.Model):
    # убрать клиента, он тут не нужен
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Почтовая рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент сервиса')
    last_try = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.BooleanField(verbose_name='Статус попытки')
    mail_service_response = models.CharField(max_length=150, verbose_name='Ответ почтового сервиса', blank=True,
                                             null=True)

    def __str__(self):
        return f'{self.mailing}: последняя попытка {self.last_try}, статус {self.status}'

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
