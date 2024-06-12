# Generated by Django 5.0.6 on 2024-06-07 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_remove_customuser_bio_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="bio",
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name="customuser",
            name="profile_photo",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]