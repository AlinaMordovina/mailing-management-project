from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from mailing.forms import MailingForm, ClientForm, MassageForm
from mailing.models import Mailing, Client, Massage, Log
#from mailing.services import get_cached_product_list


class MailingListView(ListView):
    model = Mailing

    # def get_queryset(self):
    #     return get_cached_product_list()

    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     for product in context_data.get("object_list"):
    #         product.version = product.versions.filter(is_active=True).first()
    #     return context_data


class MailingDetailView(DetailView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailing:mailing_list")

    # def form_valid(self, form):
    #     self.object = form.save()
    #     self.object.owner = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     if (
    #         self.object.owner == self.request.user
    #         or self.request.user.is_superuser is True
    #         or self.request.user.groups.filter(name="moderators").exists() is True
    #     ):
    #         return self.object
    #     raise Http404

    def get_success_url(self):
        return reverse("mailing:mailing_detail", args=[self.kwargs.get("pk")])

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data()
    #     ProductFormset = inlineformset_factory(
    #         Product, Version, form=VersionForm, extra=1
    #     )
    #     if self.request.method == "POST":
    #         context_data["formset"] = ProductFormset(
    #             self.request.POST, instance=self.object
    #         )
    #     else:
    #         context_data["formset"] = ProductFormset(instance=self.object)
    #
    #     return context_data

    # def form_valid(self, form):
    #     context_data = self.get_context_data()
    #     formset = context_data["formset"]
    #     if form.is_valid() and formset.is_valid():
    #         self.object = form.save()
    #         formset.instance = self.object
    #         formset.save()
    #         return super().form_valid(form)
    #     else:
    #         return self.render_to_response(
    #             self.get_context_data(form=form, formset=formset)
    #         )

    # def get_form_class(self):
    #     user = self.request.user
    #     if user.is_superuser or self.object.owner == user:
    #         return ProductForm
    #     elif user.groups.filter(name="moderators").exists() is True:
    #         return ProductModeratorForm


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy("mailing:mailing_list")


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailing:client_list")


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


class MassageDetailView(DetailView):
    model = Massage


class MassageCreateView(LoginRequiredMixin, CreateView):
    model = Massage
    form_class = MassageForm
    success_url = reverse_lazy("mailing:massage_list")


class MassageUpdateView(LoginRequiredMixin, UpdateView):
    model = Massage
    form_class = MassageForm

    def get_success_url(self):
        return reverse("mailing:massage_detail", args=[self.kwargs.get("pk")])


class MassageDeleteView(LoginRequiredMixin, DeleteView):
    model = Massage
    success_url = reverse_lazy("mailing:massage_list")
