# Generated by Django 4.1.2 on 2023-01-27 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0013_alter_usermembership_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='club',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='Clubs.club'),
        ),
    ]
