
from django.urls import path
from .views import (
	SettingsView, 
	CountsCreateView, 
	CountsDetailView, 
	CountsUpdateView, 
	CountsDeleteView
)

urlpatterns = [
	path("", SettingsView.as_view(), name="home"),
	path('detection/new/', CountsCreateView.as_view(), name='counts_create'),
	path("detection/<int:pk>/", CountsDetailView.as_view(), name='counts_detail'),
	path("detection/<int:pk>/edit/", CountsUpdateView.as_view(), name='counts_edit'),
	path("detection/<int:pk>/delete/", CountsDeleteView.as_view(), name='counts_delete'),
]