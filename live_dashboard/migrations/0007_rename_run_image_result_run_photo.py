# Generated by Django 3.2.4 on 2021-06-24 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('live_dashboard', '0006_alter_result_date_completed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='run_image',
            new_name='run_photo',
        ),
    ]
