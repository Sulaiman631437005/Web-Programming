# Generated by Django 4.1.1 on 2022-09-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Personal", "0007_alter_memberimages_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memberimages",
            name="image",
            field=models.ImageField(upload_to="img/%y"),
        ),
    ]