# Generated by Django 5.1.5 on 2025-02-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
