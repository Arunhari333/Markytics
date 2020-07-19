from django.urls import path
from . import views
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)

app_name = 'IncidentForm'

urlpatterns = [
    path('', views.incident_submitted, name='home'),
    path('login/', login, {'template_name': 'IncidentForm/login.html'}),
    path('logout/', logout, {'template_name': 'IncidentForm/logout.html'}),
    path('incident/', views.Incident.as_view(), name='incident'),
]
