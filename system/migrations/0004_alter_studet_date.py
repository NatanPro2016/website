# Generated by Django 4.2.5 on 2023-09-06 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0003_studet_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studet",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]