# Generated by Django 4.2.5 on 2023-10-05 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0004_prakatakepalasekolahsmp"),
    ]

    operations = [
        migrations.RenameField(
            model_name="prakatakepalasekolahsmp", old_name="foto", new_name="fotosmp",
        ),
    ]