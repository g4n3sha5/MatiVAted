# Generated by Django 4.1.2 on 2023-01-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0004_rename_contact_club_email_club_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
