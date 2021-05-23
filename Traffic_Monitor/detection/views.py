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
        def graph_function(request,object):
            in_list =[]
            out_list =[]
            x=[]
            y=[]
            x2=[]
            y2=[]
            company_name = object
            print(object, "\n")

            #Variables to store objects from models
            model = Company.objects.all()
            movement_model = Movement.objects.all()

            # iterate objects in the movement model
            for object in movement_model:

                #if company name in the model is the one asked for
                if company_name == object.company:


                    # if the iterations entry time is not NONE
                    if object.timeOut != None:
                        
                        #add the the date/time to a list
                        out_list.append(object.timeOut)
                        #y2.append(len(out_list))

                        #create a list and within it store it's hour, if the value is valid
                        x2 = [x2.hour for x2 in out_list if x2 != None]


                    # if the iterations entry time is not NONE
                    if object.timeIn != None:

                        #add the the date/time to a list
                        in_list.append(object.timeIn)
                        # y.append(len(in_list))
                        
                        #create a list and within it store the hour, if the value is valid
                        x = [x.hour for x in in_list if x != None]

            for i in x:
                y.append(x.count(i))
            for i in x2:
                y2.append(x2.count(i))
                    


            print("INLIST: ",in_list, "\n\n")
            print("INLIST Length: ",len(in_list), "\n\n")

            print("OUTLIST: ",out_list, "\n\n")
            print("OUTLIST Length: ",len(out_list), "\n\n")

            print("LIST LENGTHS: ",len(in_list),",", len(out_list))

            print("X stuffs: ",x)
            print("Y list: ", y,"\n")
            
            print("X2 stuffs: ",x2)
            print("Y2 list: ", y2,"\n")

            chart = get_plot(x, y, x2, y2, object.company)
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

