# Generated by Django 5.1.1 on 2024-10-08 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='google_meet_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
