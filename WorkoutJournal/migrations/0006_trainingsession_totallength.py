# Generated by Django 4.1.2 on 2023-02-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutJournal', '0005_alter_trainingsession_hourslength_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingsession',
            name='totalLength',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]