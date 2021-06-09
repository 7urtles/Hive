from .models import Company, Movement
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
# utils graphing import
from .utils import get_plot


class SettingsView(ListView):
    model = Company
    template_name = "home.html"
    def as_view():
        def graph_function(request):
              
            #Variables to store objects from models
            company_model = Company.objects.all()
            movement_model = Movement.objects.all()
            iterations = len(company_model)
            count = 0

            # using a counter to access the company model
            while count <= int(iterations):
                # All variables must be cleared of their data on each iteration
                in_list =[]
                out_list =[]
                x=[]
                y=[]
                x2=[]
                y2=[] 
#-----------------------------------------------------------------------------------------------------------------------------------------------------
            # This needs to be edited to load all the movements into a variable containing a list of movements for each company
            # then access the movements according to company name. Instead of iterating every single movement everytime the loop is entered.    
#-----------------------------------------------------------------------------------------------------------------------------------------------------
            # iterate objects in the movement model

                for item in movement_model:
                    #if company name in the model is the one asked for
                    company_model_name = company_model[count].company
                    if company_model_name == item.company:
                        # print("company_model_name: {}, item.company: {}".format(company_model_name, item.company))
                        # if the iterations entry time is not NONE
                        if item.timeOut != None:
                            #add the the date/time to a list
                            out_list.append(item.timeOut)
                            #create a list and within it store it's hour, if the value is valid
                            x2 = [x2.hour for x2 in out_list if x2 != None]

                        # if the iterations entry time is not NONE
                        if item.timeIn != None:
                            #add the the date/time to a list
                            in_list.append(item.timeIn)                        
                            #create a list and within it store the hour, if the value is valid
                            x = [x.hour for x in in_list if x != None]
                
                
                #count number of times entrences/exits happened per hour
                for i in x:
                    y.append(x.count(i))
                for i in x2:
                    y2.append(x2.count(i))

                if count == 0:
                    chart = get_plot(x, y, x2, y2)

                elif count == 1:
                    chart1 = get_plot(x, y, x2, y2)

                elif count == 2:
                    chart2 = get_plot(x, y, x2, y2)
                
                    return render(request, 'home.html', {'chart': chart, 'chart1': chart1,
                    'chart2': chart2, 'object_list':company_model, 'entrances':movement_model})

                count += 1
                
        return graph_function
    

class CompanyDetailView(DetailView):
	model = Company
	template_name = 'home.html'

class CompanyCreateView(CreateView):
    model = Company
    template_name = 'company_create.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'edit.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']
    success_url = reverse_lazy('home')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_reset.html'
    success_url = reverse_lazy('home')

