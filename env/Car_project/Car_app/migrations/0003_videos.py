# Generated by Django 5.1 on 2024-08-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car_app', '0002_fruits'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('video', models.FileField(upload_to='videos/')),
            ],
        ),
    ]
