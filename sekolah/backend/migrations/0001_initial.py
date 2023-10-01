# Generated by Django 4.2.5 on 2023-09-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrakataKepalaSekolah",
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
                ("judul", models.CharField(max_length=255)),
                ("keterangan", models.TextField()),
                ("foto", models.ImageField(upload_to="foto/")),
            ],
        ),
        migrations.CreateModel(
            name="Sejarah",
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
                ("judul", models.CharField(max_length=255)),
                ("keterangan", models.TextField()),
                ("foto", models.ImageField(upload_to="foto/")),
            ],
        ),
        migrations.CreateModel(
            name="StrukturOrganisasi",
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
                ("nama", models.CharField(max_length=255)),
                ("jabatan", models.TextField()),
                ("foto", models.ImageField(upload_to="foto/")),
            ],
        ),
        migrations.CreateModel(
            name="VisidanMisi",
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
                ("judul", models.CharField(max_length=255)),
                ("keterangan", models.TextField()),
                ("foto", models.ImageField(upload_to="foto/")),
            ],
        ),
    ]