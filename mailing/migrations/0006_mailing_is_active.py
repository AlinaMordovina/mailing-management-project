# Generated by Django 5.0.3 on 2024-04-15 14:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mailing", "0005_alter_mailing_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активация рассылки"),
        ),
    ]
