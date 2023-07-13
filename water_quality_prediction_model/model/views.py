from django.shortcuts import render
import os
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        ph = request.POST['Ph']
        hardness = request.POST['Hardness']
        solids = request.POST['Solids']
        chloramines = request.POST['Chloramines']
        sulfate = request.POST['Sulfate']
        conductivity = request.POST['Conductivity']
        organic_carbon = request.POST['Organic_carbon']
        trihalomethanes = request.POST['Trihalomethanes']
        turbidity = request.POST['Turbidity']

        with open("C:\\Users\\kunda\\Desktop\\ML\\Kundan\\assignments\\water_quality\\water_quality_prediction_model\\model\\water_prediction", 'rb') as f:
            model = pickle.load(f)
            prediction = model.predict([[ph,hardness,solids,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity]])
        if prediction==0:
            msg = "Your water is safe to drink"
        else:
            msg = "Your water is not safe to drink"
    return render(request, 'result.html',{'result':msg})