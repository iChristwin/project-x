# Generated by Django 4.1.3 on 2022-12-04 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
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
                ("name", models.CharField(max_length=200)),
                ("titles", models.CharField(max_length=200)),
                ("location", models.CharField(max_length=200)),
                ("school", models.CharField(max_length=200)),
            ],
        ),
    ]
