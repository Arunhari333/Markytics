# Generated by Django 2.0.3 on 2020-07-09 19:49

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
            name='incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.IntegerField(choices=[(1, 'Corporate Headoffice'), (2, 'Location2'), (3, 'Location3'), (4, 'Location4')])),
                ('description', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('incidentLoc', models.CharField(blank=True, max_length=500, null=True)),
                ('severity', models.IntegerField(choices=[(1, 'Low'), (2, 'Moderate'), (3, 'High')], default=0)),
                ('cause', models.CharField(blank=True, max_length=100, null=True)),
                ('actionTaken', models.CharField(max_length=100)),
                ('subIncidentTypes', models.IntegerField(blank=True, choices=[(1, 'Environmental Incident'), (2, 'Injury/Illness'), (3, 'Property Damage'), (4, 'Vehicle')], null=True)),
                ('reportedBy', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]