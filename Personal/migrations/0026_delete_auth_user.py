# Generated by Django 4.1.2 on 2022-10-07 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Personal", "0025_auth_user"),
    ]

    operations = [
        migrations.DeleteModel(name="Auth_user",),
    ]