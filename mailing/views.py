from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)

from blog.models import Blog
from mailing.forms import MailingForm, ClientForm, MassageForm
from mailing.models import Mailing, Client, Massage
from mailing.services import get_cache_for_mailings


class HomePageView(TemplateView):
    template_name = 'mailing/home_page.html'
    extra_context = {
        'title': 'Главная',
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailing_count'] = get_cache_for_mailings()
        context_data['active_mail_count'] = Mailing.objects.filter(is_active=True).count()
        context_data['client_count'] = Client.objects.all().count()
        context_data['object_list'] = Blog.objects.filter(date_is_published__isnull=False)[:3]

        return context_data


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self, **kwargs):
        if not self.request.user.is_authenticated:
            return Mailing.objects.filter(owner=None)
        elif self.request.user.is_superuser or self.request.user.groups.filter(name="managers").exists() is True:
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if (
            self.object.owner == self.request.user
            # or self.request.user.is_superuser is True
            # or self.request.user.groups.filter(name="moderators").exists() is True
        ):
            return self.object
        raise Http404

    def get_success_url(self):
        return reverse("mailing:mailing_detail", args=[self.kwargs.get("pk")])


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


class ClientListView(ListView):
    model = Client

    def get_queryset(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Client.objects.all()
        return Client.objects.filter(owner=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse("mailing:client_detail", args=[self.kwargs.get("pk")])


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("mailing:client_list")


class MassageListView(ListView):
    model = Massage

    def get_queryset(self, **kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return Massage.objects.all()
        return Massage.objects.filter(owner=self.request.user)


class MassageDetailView(LoginRequiredMixin, DetailView):
    model = Massage


class MassageCreateView(LoginRequiredMixin, CreateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy("mailing:massage_list")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class MassageUpdateView(LoginRequiredMixin, UpdateView):
    model = Massage
    form_class = MassageForm

    def get_success_url(self):
        return reverse("mailing:massage_detail", args=[self.kwargs.get("pk")])


class MassageDeleteView(LoginRequiredMixin, DeleteView):
    model = Massage
    success_url = reverse_lazy("mailing:massage_list")


def update_mailing_activity(request, pk):
    mail_item = get_object_or_404(Mailing, pk=pk)
    if mail_item.is_active:
        mail_item.is_active = False
    else:
        mail_item.is_active = True
    mail_item.save()
    return redirect('mailing:mailing_list')
