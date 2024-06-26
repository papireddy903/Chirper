# Generated by Django 5.0.6 on 2024-06-12 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_rename_tweeted_by_chirp_author_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="like",
            old_name="author",
            new_name="liked_by",
        ),
        migrations.CreateModel(
            name="Reply",
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
                ("text", models.TextField(max_length=1000)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="chirp_author",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "chirp",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="base.chirp"
                    ),
                ),
                (
                    "replied_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="replied_by",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
