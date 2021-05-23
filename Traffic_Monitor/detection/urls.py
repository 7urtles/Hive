from django.urls import path
from .views import (
	SettingsView, 
	CompanyCreateView, 
	CompanyDetailView, 
	CompanyUpdateView, 
	CompanyDeleteView,
	GraphView,
)

urlpatterns = [
	path("", SettingsView.as_view(), name="home"),
	path("graph/<str:object>/", GraphView.as_view(), name="graph"),
	path('detection/new/', CompanyCreateView.as_view(), name='company_create'),
	path("detection/<int:pk>/", CompanyDetailView.as_view(), name='company_detail'),
	path("detection/<int:pk>/edit/", CompanyUpdateView.as_view(), name='company_edit'),
	path("detection/<int:pk>/delete/", CompanyDeleteView.as_view(), name='company_delete'),
]