# Generated by Django 3.2.2 on 2024-03-21 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20240321_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialpost',
            name='shared_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
