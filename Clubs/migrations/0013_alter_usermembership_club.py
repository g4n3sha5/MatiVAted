# Generated by Django 4.1.2 on 2023-01-25 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Clubs', '0012_usermembership_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermembership',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membersClub', to='Clubs.club'),
        ),
    ]
