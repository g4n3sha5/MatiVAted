# Generated by Django 4.1.2 on 2022-11-03 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Journal', '0002_alter_todolist_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todolist', to=settings.AUTH_USER_MODEL),
        ),
    ]
