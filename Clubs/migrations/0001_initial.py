# Generated by Django 4.1.2 on 2023-01-09 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, default='defaultLogo.png', null=True, upload_to='clubs_logo')),
                ('estabilished', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, max_length=2500, null=True)),
                ('contact', models.TextField(blank=True, max_length=100, null=True)),
                ('instructors', models.TextField(blank=True, max_length=100, null=True)),
                ('authorizedUser', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
