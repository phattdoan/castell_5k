# Generated by Django 3.2.4 on 2021-06-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_dashboard', '0005_auto_20210624_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]