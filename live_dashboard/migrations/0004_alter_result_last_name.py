# Generated by Django 3.2.4 on 2021-06-24 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('live_dashboard', '0003_alter_result_age_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
