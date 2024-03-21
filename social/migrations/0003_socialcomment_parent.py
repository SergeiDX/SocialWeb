# Generated by Django 3.2.2 on 2024-03-20 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_socialcomment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialcomment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.socialcomment'),
        ),
    ]
