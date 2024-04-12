from django.contrib import admin

from mailing.models import Client, Mailing, Massage, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'lastname', 'firstname', 'middlename', 'email',)
    search_fields = ('lastname', 'firstname', 'email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'start_time', 'end_time', 'request_period', 'status',)
    list_filter = ('start_time', 'end_time', 'request_period', 'status',)


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject', 'mailing',)
    search_fields = ('subject', 'body',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'mailing', 'last_try', 'status', 'mail_service_response',)
    list_filter = ('mailing', 'status',)
    search_fields = ('last_try',)
