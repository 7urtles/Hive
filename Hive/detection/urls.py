from django.urls import path
from .views import (
	SettingsView, 
	CompanyCreateView, 
	CompanyDetailView, 
	CompanyUpdateView, 
	CompanyDeleteView,
)

urlpatterns = [
	path("", SettingsView.as_view(), name="home"),
	path('detection/new/', CompanyCreateView.as_view(), name='company_create'),
	path("detection/<int:pk>/", CompanyDetailView.as_view(), name='company_detail'),
	path("detection/<int:pk>/edit/", CompanyUpdateView.as_view(), name='edit'),
	path("detection/<int:pk>/delete/", CompanyDeleteView.as_view(), name='company_delete'),
]