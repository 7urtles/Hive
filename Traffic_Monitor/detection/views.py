from .models import Counting
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
# Create your views here.

class SettingsView(ListView):
    model = Counting
    template_name = "home.html"

class CountsDetailView(DetailView):
	model = Counting
	template_name = 'home.html'

class CountsCreateView(CreateView):
    model = Counting
    template_name = 'counts_create.html'
    fields = ['company', 'entered', 'exited', 'current_total', 'building_capacitiy']

class CountsUpdateView(UpdateView):
    model = Counting
    template_name = 'counts_edit.html'
    fields = ['company', 'entered', 'exited', 'current_total', 'building_capacitiy']

class CountsDeleteView(DeleteView):
    model = Counting
    template_name = 'settings_reset.html'
    success_url = reverse_lazy('home')