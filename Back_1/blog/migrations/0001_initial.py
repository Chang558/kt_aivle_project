# Generated by Django 3.2.19 on 2023-06-21 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]