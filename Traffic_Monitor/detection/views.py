from .models import Counting
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
    fields = ['company', 'entered', 'exited', 'current', 'capacity']

class CountsUpdateView(UpdateView):
    model = Counting
    template_name = 'counts_edit.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']
    success_url = reverse_lazy('home')

class CountsDeleteView(DeleteView):
    model = Counting
    template_name = 'counts_reset.html'
    success_url = reverse_lazy('home')