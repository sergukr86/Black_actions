# Generated by Django 4.2.5 on 2023-10-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="birth_date",
            field=models.DateField(default="1999-12-12", verbose_name="date of birth"),
            preserve_default=False,
        ),
    ]