# Generated by Django 3.2.18 on 2023-09-20 19:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('minestructure', '0069_auto_20230920_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blueprintsharelinkmodel',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 27, 19, 38, 30, 573707, tzinfo=utc)),
        ),
    ]
