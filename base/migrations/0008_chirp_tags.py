# Generated by Django 5.0.6 on 2024-06-15 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0007_follow"),
    ]

    operations = [
        migrations.AddField(
            model_name="chirp",
            name="tags",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
