# Generated by Django 5.0.6 on 2025-03-03 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0002_ebook_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='verified',
        ),
    ]
