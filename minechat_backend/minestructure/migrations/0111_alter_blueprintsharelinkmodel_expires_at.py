# Generated by Django 3.2.18 on 2024-01-11 19:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('minestructure', '0110_alter_blueprintsharelinkmodel_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprintsharelinkmodel',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 18, 19, 37, 49, 861877, tzinfo=utc)),
        ),
    ]
