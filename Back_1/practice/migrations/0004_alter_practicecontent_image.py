# Generated by Django 3.2.19 on 2023-06-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0003_predict_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practicecontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='practice'),
        ),
    ]
