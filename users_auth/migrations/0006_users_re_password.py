# Generated by Django 2.1 on 2020-03-27 22:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0005_merge_20200327_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='re_password',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
