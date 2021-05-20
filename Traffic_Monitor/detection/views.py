from .models import Counting
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
# utils graphing import
from .utils import get_plot


# Create your views here.
class GraphView(ListView):
    template_name = "graph.html"
    def as_view():
        def graph_function(request):
            model = Counting.objects.all()
            qs = Counting.objects.all()
            x = [x.company for x in qs]
            y = [y.current for y in qs]
            chart = get_plot(x, y)
            return render(request, 'graph.html', {'chart': chart, 'object_list':model})
        return graph_function

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

