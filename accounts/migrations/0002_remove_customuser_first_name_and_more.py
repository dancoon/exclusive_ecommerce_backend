# Generated by Django 5.0.1 on 2024-01-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="customuser",
            name="last_name",
        ),
        migrations.AddField(
            model_name="customuser",
            name="name",
            field=models.CharField(default=1, max_length=50, verbose_name="Name"),
            preserve_default=False,
        ),
    ]
