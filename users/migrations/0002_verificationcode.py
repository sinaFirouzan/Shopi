# Generated by Django 5.1.5 on 2025-02-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('code', models.CharField(max_length=4, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
