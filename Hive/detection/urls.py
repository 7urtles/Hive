from django.urls import path
from .views import (
	SettingsView, 
	CompanyUpdateView, 
)

urlpatterns = [
	path("", SettingsView.as_view(), name="home"),
	path("detection/<int:pk>/edit/", CompanyUpdateView.as_view(), name='edit'),
]