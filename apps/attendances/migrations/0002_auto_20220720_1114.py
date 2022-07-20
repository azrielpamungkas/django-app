# Generated by Django 3.2.13 on 2022-07-20 04:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 7, 20, 4, 14, 21, 82775, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_mode',
            field=models.SmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='leave',
            name='leave_type',
            field=models.SmallIntegerField(blank=True),
        ),
    ]
