# Generated by Django 3.1.1 on 2020-10-06 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0003_auto_20201006_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrlaggregatedblockdata',
            name='block_found_time_average',
        ),
    ]