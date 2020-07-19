from django import forms
from .models import incident

class IncidentForm(forms.ModelForm):
    CHOICE = ((1, 'Corporate Headoffice'), (2, 'Operations Department'), (3, 'Work Station'), (4, 'Marketing Division'))
    CHOICE1 = ((1, 'Mild'), (2, 'Moderate'), (3, 'Severe'))
    CHOICE2 = (('1', 'Environmental Incident'), ('2', 'Injury/Illness'), ('3', 'Property Damage'), ('4', 'Vehicle'))
    location = forms.ChoiceField(choices=CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
    severity = forms.ChoiceField(choices=CHOICE1, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = incident
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'incidentLoc': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'cause': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'actionTaken': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'reportedBy': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'value': ''}),
        }
