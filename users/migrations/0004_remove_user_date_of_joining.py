# Generated by Django 5.1.5 on 2025-02-06 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_verificationcode_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_of_joining',
        ),
    ]
