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
            company_model = Company.objects.all()
            movement_model = Movement.objects.all()

            # iterate objects in the movement model
            for item in movement_model:

                #if company name in the model is the one asked for
                if company_name == item.company:

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

            print("X: ", x, 'Y :', y, "X2 :", x2, "Y2 :", y2)

            chart = get_plot(x, y, x2, y2)
            return render(request, 'graph.html', {'chart': chart, 'object_list':company_model, 'entrances':movement_model})
        return graph_function

class SettingsView(ListView):
    model = Company
    template_name = "home.html"
    def as_view():
        def graph_function(request):
            in_list =[]
            out_list =[]
            
            #Variables to store objects from models
            company_model = Company.objects.all()
            movement_model = Movement.objects.all()
            iterations = len(company_model)
            count = 0

            # using a counter to access the company model
            while count <= iterations:
                x=[]
                y=[]
                x2=[]
                y2=[]
            # iterate objects in the movement model
                for item in movement_model:
                    #if company name in the model is the one asked for
                    print("looking here------------------> ",movement_model[count].company,"isnt equal to", item.company,"?")
                    company_model_name = company_model[count].company
                    if company_model_name == item.company:
                        print('entered if as :',company_model_name)
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
                print("X: ", x, 'Y :', y, "X2 :", x2, "Y2 :", y2)
                if count == 0:
                    chart = get_plot(x, y, x2, y2)
                    print('CHART 1 SAVED')
                if count == 1:
                    chart1 = get_plot(x, y, x2, y2)
                    print('CHART 2 SAVED')
                    return render(request, 'home.html', {'chart': chart, 'chart1': chart1, 'object_list':company_model, 'entrances':movement_model})
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
    template_name = 'company_edit.html'
    fields = ['company', 'entered', 'exited', 'current', 'capacity']
    success_url = reverse_lazy('home')

class CompanyDeleteView(DeleteView):
    model = Company
    template_name = 'company_reset.html'
    success_url = reverse_lazy('home')

