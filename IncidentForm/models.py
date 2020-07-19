from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class incident(models.Model):
    user = models.ForeignKey(User, models.CASCADE, blank=True, null=True)
    CHOICE = ((1, 'Corporate Headoffice'), (2, 'Operations Department'), (3, 'Work Station'), (4, 'Marketing Division'))
    location = models.IntegerField(choices=CHOICE)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    time = models.TimeField()
    incidentLoc = models.CharField(max_length=500, blank=True, null=True)
    CHOICE1 = ((1, 'Mild'), (2, 'Moderate'), (3, 'Severe'))
    severity = models.IntegerField(choices=CHOICE1, default=0)
    cause = models.CharField(max_length=100, blank=True, null=True)
    actionTaken = models.CharField(max_length=100, blank=True, null=True)
    CHOICE2 = (('1', 'Environmental Incident'), ('2', 'Injury/Illness'), ('3', 'Property Damage'), ('4', 'Vehicle'))
    subIncidentTypes = MultiSelectField(choices=CHOICE2)
    reportedBy = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
