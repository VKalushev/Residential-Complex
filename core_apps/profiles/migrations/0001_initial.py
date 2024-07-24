# Generated by Django 4.2.11 on 2024-07-24 18:36

import autoslug.fields
import cloudinary.models
import core_apps.profiles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("id", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now_add=True)),
                (
                    "avatar",
                    cloudinary.models.CloudinaryField(
                        blank=True, max_length=255, null=True, verbose_name="Avatar"
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("male", "Male"),
                            ("female", "Female"),
                            ("other", "Other"),
                        ],
                        default="other",
                        max_length=10,
                        verbose_name="Gender",
                    ),
                ),
                ("bio", models.TextField(blank=True, null=True, verbose_name="Bio")),
                (
                    "occupation",
                    models.CharField(
                        choices=[
                            ("mason", "Mason"),
                            ("carpenter", "Carpenter"),
                            ("plumber", "Plumber"),
                            ("roofer", "Roofer"),
                            ("painter", "Painter"),
                            ("electrician", "Electrician"),
                            ("hvac", "HVAC"),
                            ("tenant", "Tenant"),
                        ],
                        default="tenant",
                        max_length=20,
                        verbose_name="Occupation",
                    ),
                ),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        default="+250784123456",
                        max_length=30,
                        region=None,
                        verbose_name="Phone Number",
                    ),
                ),
                (
                    "country_of_origin",
                    django_countries.fields.CountryField(
                        default="KE", max_length=2, verbose_name="Country"
                    ),
                ),
                (
                    "city_of_origin",
                    models.CharField(
                        default="Nairobi", max_length=180, verbose_name="City"
                    ),
                ),
                (
                    "report_count",
                    models.IntegerField(default=0, verbose_name="Report Count"),
                ),
                (
                    "reputation",
                    models.IntegerField(default=100, verbose_name="Reputation"),
                ),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        populate_from=core_apps.profiles.models.get_user_username,
                        unique=True,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at", "-updated_at"],
                "abstract": False,
            },
        ),
    ]
