from django.shortcuts import render, redirect, get_object_or_404
from .forms import IncidentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import incident
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.
class Incident(LoginRequiredMixin, TemplateView):
    template_name = 'IncidentForm/incident.html'

    def get(self, request):
        form = IncidentForm()
        reportedBy = str(request.user)
        form.fields['reportedBy'].widget.attrs['value'] = reportedBy
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = IncidentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()

            messages.success(request, 'Incident Reported')
            return redirect('/incidentform/')

        return render(request, self.template_name, {'form': form})

@login_required
def incident_submitted(request):
    return render(request, 'IncidentForm/home.html', {'user': request.user})
