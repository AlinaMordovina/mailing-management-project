from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mailing.apps import MailingConfig

from mailing.views import (MailingCreateView, MailingDeleteView,
                           MailingDetailView, MailingListView, MailingUpdateView,
                           ClientListView, ClientCreateView, ClientUpdateView,
                           ClientDetailView, ClientDeleteView,
                           MassageListView, MassageCreateView, MassageUpdateView,
                           MassageDetailView, MassageDeleteView, HomePageView, update_mailing_activity)

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),

    path("mailing/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("mailing/create", MailingCreateView.as_view(), name="mailing_create"),
    path(
        "mailing/<int:pk>/update", MailingUpdateView.as_view(), name="mailing_update"
    ),
    path(
        "mailing/<int:pk>/delete", MailingDeleteView.as_view(), name="mailing_delete"
    ),
    path('mailing/activity/<int:pk>/', update_mailing_activity, name='update_mailing_activity'),

    path("client/", ClientListView.as_view(), name="client_list"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client/create", ClientCreateView.as_view(), name="client_create"),
    path(
        "client/<int:pk>/update", ClientUpdateView.as_view(), name="client_update"
    ),
    path(
        "client/<int:pk>/delete", ClientDeleteView.as_view(), name="client_delete"
    ),

    path("massage/", MassageListView.as_view(), name="massage_list"),
    path("massage/<int:pk>/", MassageDetailView.as_view(), name="massage_detail"),
    path("massage/create", MassageCreateView.as_view(), name="massage_create"),
    path(
        "massage/<int:pk>/update", MassageUpdateView.as_view(), name="massage_update"
    ),
    path(
        "massage/<int:pk>/delete", MassageDeleteView.as_view(), name="massage_delete"
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
