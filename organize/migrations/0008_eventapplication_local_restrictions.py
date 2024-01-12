# Generated by Django 3.2.7 on 2022-03-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organize", "0007_auto_20210906_1216"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventapplication",
            name="local_restrictions",
            field=models.TextField(
                blank=True,
                verbose_name="Information about local restrictions for physical restrictions due to Covid-19 pandemic.",
            ),
        ),
    ]
