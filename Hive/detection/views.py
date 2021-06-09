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

            # Using counter to access the company model
            count = 0

            # Contains objects needed to render data on page
            returned_objects_dictionary = {'object_list':company_model, 'entrances':movement_model}

            while count < int(iterations):
                # These lists must be cleared of their data on each iteration
                in_list =[]
                out_list =[]
                x=[]
                y=[]
                x2=[]
                y2=[]

#-----------------------------------------------------------------------------------------------------------------------------------------------------
            # This needs to be refactored to load all the movements into a variable containing a list of movements for each company
            # then access the movements according to company name. Instead of iterating every single movement everytime the loop is entered.    
#-----------------------------------------------------------------------------------------------------------------------------------------------------
                for item in movement_model:
                    #if company name in the model is the one asked for
                    company_model_name = company_model[count].company
                    if company_model_name == item.company:

                        # if the iterations entry time exists
                        if item.timeOut:
                            #add the the date/time to a list
                            out_list.append(item.timeOut)
                            #create a list and within it store it's hour
                            x2 = [x2.hour for x2 in out_list]

                        # if the iterations entry time exists
                        if item.timeIn:
                            #add the the date/time to a list
                            in_list.append(item.timeIn)                        
                            #create a list and within it store the hour
                            x = [x.hour for x in in_list]
                
                #count number of times entrences/exits happened per hour
                for i in x:
                    y.append(x.count(i))
                for i in x2:
                    y2.append(x2.count(i))

                # Dynamic string creation
                chart_name = "chart{}".format(count)

                # Dynamic variable creation
                globals()["chart{}".format(count)] = get_plot(x, y, x2, y2)

                # Append Dynamic variable to the dictionary
                returned_objects_dictionary[chart_name] = globals()["chart{}".format(count)]

                count += 1
            return render(request, 'home.html', returned_objects_dictionary)   
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

