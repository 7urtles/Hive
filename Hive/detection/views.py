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
            company_model,movement_model,iterations = Company.objects.all(),Movement.objects.all(),len(Company.objects.all())
            # Contains objects needed to render data on page
            returned_objects_dictionary = {'object_list':company_model, 'entrances':movement_model}
#-----------------------------------------------------------------------------------------------------------------------------------------------------
            # The below loops need to be refactored to load all the movements into a variable containing a list of movements for each company.
            # Then access the movements according to company name. Instead of iterating every single movement everytime the loop is entered.    
#-----------------------------------------------------------------------------------------------------------------------------------------------------
            # Using counter to access the company model
            count = 0
            while count < int(iterations):
                # These lists must be cleared of their data on each iteration
                in_list,out_list ,x ,y ,x2 ,y2 = [],[],[],[],[],[]
                company_model_name = company_model[count].company
                #if the company name of the company_model & movement_model is the same
                movements =[item for item in movement_model if company_model_name == item.company]
                count2=0
                while count2 < len(movements):
                    # if the iterations entry time exists
                    if movements[count2].timeOut:
                        out_list.append(movements[count2].timeOut)
                        #create a list and within it store it's hour
                        x2 = [x2.hour for x2 in out_list]
                    # if the iterations entry time exists
                    if movements[count2].timeIn:
                        in_list.append(movements[count2].timeIn)                        
                        #create a list and within it store the hour
                        x = [x.hour for x in in_list]
                    count2+=1
                #count number of times entrences/exits happened per hour
                y,y2 = [x.count(i) for i in x],[x2.count(i) for i in x2]
                # Dynamic string creation
                chart_name = "chart{}".format(count)
                # Dynamic variable creation
                globals()["chart{}".format(count)] = get_plot(x, y, x2, y2)
                # Append created variable to dictionary
                returned_objects_dictionary[chart_name] = globals()["chart{}".format(count)]
                count += 1
            return render(request, 'home.html', returned_objects_dictionary)   
        return graph_function

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = 'edit.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']
    success_url = reverse_lazy('home')