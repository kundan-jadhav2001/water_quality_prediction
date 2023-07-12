from django.shortcuts import render
import os,pickle
import sklearn
import numpy as np 
import matplotlib.pyplot as plt

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        ph = request.POST['ph']
        hardness = request.POST['hardness']
        solids = request.POST['solids']
        chloramines = request.POST['chloramines']
        sulfate = request.POST['sulfate']
        conductivity = request.POST['conductivity']
        organic_carbon = request.POST['organic_carbon']
        trihalomethanes = request.POST['trihalomethanes']
        turbidity = request.POST['turbidity']

        with open("C:\\Users\\kunda\\Desktop\\ML\\Kundan\\assignments\\water_quality\\water_quality_prediction_model\\model\\model_pre", 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict([[ph,hardness,solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]])
            print(prediction)

    return render(request, 'result.html',{'result':prediction})