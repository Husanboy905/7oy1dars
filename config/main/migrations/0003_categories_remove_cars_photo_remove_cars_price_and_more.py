# Generated by Django 5.1.6 on 2025-03-05 14:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_rename_color_brands_rename_car_cars_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Categories",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="cars",
            name="photo",
        ),
        migrations.RemoveField(
            model_name="cars",
            name="price",
        ),
        migrations.RemoveField(
            model_name="cars",
            name="speed",
        ),
        migrations.RemoveField(
            model_name="cars",
            name="year",
        ),
        migrations.AlterField(
            model_name="cars",
            name="brand",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.brands"
            ),
        ),
        migrations.AlterField(
            model_name="cars",
            name="color",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.colors"
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.cars"
            ),
        ),
    ]
