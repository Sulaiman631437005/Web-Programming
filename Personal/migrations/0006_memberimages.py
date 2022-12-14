# Generated by Django 4.1.1 on 2022-09-20 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Personal", "0005_delete_auth_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberImages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="Personal/static/images/%y")),
                ("name", models.CharField(max_length=200)),
                ("text", models.CharField(max_length=500)),
            ],
        ),
    ]
