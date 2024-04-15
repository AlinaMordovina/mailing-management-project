from django.forms import BooleanField, ModelForm

from mailing.models import Client, Mailing, Massage


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        exclude = (
            "created_at",
            "last_mailing",
        )


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class MassageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Massage
        fields = "__all__"
