# Generated by Django 2.0.3 on 2020-07-10 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IncidentForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
