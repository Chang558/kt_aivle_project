# Generated by Django 3.2.19 on 2023-06-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0002_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predict_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prediction', models.CharField(max_length=500)),
                ('ground_truth', models.CharField(max_length=500)),
                ('confidence', models.FloatField()),
                ('is_correct', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]