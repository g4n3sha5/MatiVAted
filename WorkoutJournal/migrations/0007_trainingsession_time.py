# Generated by Django 4.1.2 on 2023-02-18 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutJournal', '0006_trainingsession_totallength'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]