# Generated by Django 4.1.2 on 2022-12-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutJournal', '0003_alter_trainingsession_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingsession',
            name='notes',
            field=models.TextField(max_length=2500),
        ),
    ]
