# Generated by Django 3.2.13 on 2022-06-02 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0006_alter_timetable_token'),
        ('attendances', '0005_studentattendance_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentattendance',
            name='timetable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetables.timetable'),
        ),
    ]
