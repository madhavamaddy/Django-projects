# Generated by Django 5.1 on 2024-08-22 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
