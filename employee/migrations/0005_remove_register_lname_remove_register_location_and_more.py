# Generated by Django 4.1.4 on 2022-12-14 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "employee",
            "0004_subscribe_alter_register_email_alter_register_f1name_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(model_name="register", name="lname",),
        migrations.RemoveField(model_name="register", name="location",),
        migrations.RemoveField(model_name="register", name="sgrade",),
        migrations.RemoveField(model_name="register", name="ssubject",),
        migrations.RemoveField(model_name="register", name="zip",),
        migrations.RemoveField(model_name="tutor", name="experience",),
        migrations.RemoveField(model_name="tutor", name="lname",),
        migrations.RemoveField(model_name="tutor", name="location",),
        migrations.RemoveField(model_name="tutor", name="sgrade",),
        migrations.RemoveField(model_name="tutor", name="ssubject",),
        migrations.RemoveField(model_name="tutor", name="zip",),
    ]
