# Generated by Django 3.1.4 on 2020-12-30 14:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EnvergaDB', '0003_auto_20201230_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='date_modified',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date Modified'),
        ),
    ]