# Generated by Django 4.2.2 on 2023-06-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("coplate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="nickname",
            field=models.CharField(max_length=15, null=True, unique=True),
        ),
    ]
