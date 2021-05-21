from .models import Company, Movement
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
# utils graphing import
from .utils import get_plot

# # Create your views here.
# class GraphView(ListView):
#     template_name = "graph.html"
#     def as_view():
#         def graph_function(request,pk):
#             model = Company.objects.all()
#             x = [x.company for x in model]
#             y = [y.current for y in model]
#             chart = get_plot(x, y)
#             return render(request, 'graph.html', {'chart': chart, 'object_list':model})
#         return graph_function

class GraphView(DetailView):
    template_name = "graph.html"
    def as_view():
        def graph_function(request,company):
            company_name = company
            model = Company.objects.all()
            movement_model = Movement.objects.all()
            for company in movement_model:
                if company_name == company.company:
                    x = ['Entered']
                    y = [company.timeIn.day for y in model]
                    chart = get_plot(x, y, company.company)
            return render(request, 'graph.html', {'chart': chart, 'object_list':model, 'entrances':movement_model})
        return graph_function

class SettingsView(ListView):
    model = Company
    template_name = "home.html"
    

class CompanyDetailView(DetailView):
	model = Company
	template_name = 'home.html'

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company_create.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'company_edit.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']
    success_url = reverse_lazy('home')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_reset.html'
    success_url = reverse_lazy('home')

