# Generated by Django 3.2.18 on 2023-09-12 02:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('minestructure', '0035_alter_blueprintsharelinkmodel_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprintsharelinkmodel',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 2, 19, 57, 243565, tzinfo=utc)),
        ),
    ]
