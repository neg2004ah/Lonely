# Generated by Django 4.2.7 on 2024-02-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_alter_portfolio_project_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="project_date",
            field=models.DateTimeField(),
        ),
    ]
