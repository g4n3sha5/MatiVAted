# Generated by Django 4.1.2 on 2023-02-15 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0016_alter_usermembership_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='authorized',
            field=models.CharField(choices=[('FULL', 'FULL'), ('TRAININGS', 'TRAININGS'), ('NON-AUTHORIZED', 'NON-AUTHORIZED')], default='NON-AUTHORIZED', max_length=30),
        ),
    ]
