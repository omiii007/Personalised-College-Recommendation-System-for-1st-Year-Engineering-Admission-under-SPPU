from django.db import IntegrityError
import pandas as pd
import os
import requests
import numpy as np
from django.contrib.auth.models import User
import os
from joblib import dump , load
import pickle
from django.contrib import messages
from django.shortcuts import render, redirect  
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def index(request):
        return render(request, 'index.html')
        
def input(request):
    return render(request, 'input.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('input')
        
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect('input')
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.success(request, "logged out successfully")
    return redirect('login')
   



def result(request):
        # Initialize variables before the if statement
        category_upper = ""
        department_upper = ""
        percentile = ""
        college_name = ""
        if request.method == 'POST':
            # user_input = []       
            # # Receive data from client
            # user_input.append(request.GET['Category'])
            # user_input.append(request.GET['department'])
            # user_input.append(request.GET['Year'])
            # user_input.append(request.GET['MHT_CET_Percentile'])
            category = request.POST['Category']
            department = request.POST['department']
            year = request.POST['Year']
            mht_cet_percentile = request.POST['MHT_CET_Percentile']
            
			
            
            print(category,department,year,mht_cet_percentile) 
              
            import pandas as pd 
            df = pd.read_csv("projectApp/dataset.csv")
            print(df.head())


            #user_input = ['OPEN', 'Computer Engineering', '2022', '85']
            c = category
            d = department
            y = int(year)  # Convert 'Year' to an integer

            # Convert 'Category' and 'department' to lowercase and remove spaces
            category = c.lower().replace(' ', ' ')
            department = d.lower().replace(' ', ' ')

            # Define ranges and corresponding labels
            ranges = [(0, 100)]
            labels = ['0-100']

            # Find the matching range label
            matching_label = None
            for r, label in zip(ranges, labels):
                if r[0] <= float(mht_cet_percentile) < r[1]:
                    matching_label = label
                    break
            # Initialize matching_data before the if statement
            matching_data = None
            # Filter the dataset based on the user-input criteria and matching range
            if matching_label:
                filtered_df = df[
                    (df['Category'].str.lower().str.replace(' ', ' ') == category) &
                    (df['department'].str.lower().str.replace(' ', ' ') == department) &
                    (df['Year'] == y) &
                    (df['MHT_CET_Percentile'] <= float(mht_cet_percentile))
                ]

                # Check if the filtered DataFrame is not empty
                if not filtered_df.empty:
                    matching_data = filtered_df[['Collage_name', 'MHT_CET_Percentile']]

                # Print the matching data
                if matching_data is not None and not matching_data.empty:

                    print("Matching Colleges:")
                    for i, (college_name, percentile) in enumerate(matching_data.itertuples(index=False), 1):
                        category_upper = category.upper()
                        department_upper = department.upper()
                        college_name=college_name
                        percentile=percentile
                        print(f"Sr. No.: {i}, Category: {category.upper()}, Department: {department.upper()}, College Name: {college_name}, MHT_CET_Percentile: {percentile}")
                else:
                    print("No colleges found for the specified criteria.")
            else:
                print("MHT_CET_Percentile value does not fall within predefined ranges.")

           # Category
            if category=="open":
                 category=0
            elif category=="obc":
                 category=1
            elif category=="nt":
                 category=2
            elif category=="vjnt":
                 category=3
            elif category=="sc":
                 category=4
            elif category=="st":
                category=5
            elif category=="ews":
                category=6
            else:
                category=7
            # department
            if  department=="computerengineering":
                 department=0
            elif  department=="civilengineering":
                 department=1
            elif department=="information technology":
                department=2
            elif department=="mechanicalengineering":
                department=3
            else:
                department=4
            # Traning model
            from joblib import load
            model=load('projectApp\DT.joblib')
            
            # Make prediction
            result = model.predict([[category,department,year,mht_cet_percentile]])
            print(str(result[0]))
            result1 = str(result[0])
            value1 = None  # Initialize value1 with None

            # if result=='DrDYPatil College Of Engineering and InnovationTalegaon':
            #     print("DrDYPatil College Of Engineering and InnovationTalegaon")
            #     value1 = 'DrDYPatil College Of Engineering and InnovationTalegaon'
            
            # elif result=="JSPM's Imperial College of Engineering and Research Wagholi Pune":
            #     print("JSPM's Imperial College of Engineering and Research Wagholi Pune")
            #     value1 = "JSPM's Imperial College of Engineering and Research Wagholi Pune"
            
            # elif result[0]=='Indira College of Engineering and Management Pune':
            #     print("Indira College of Engineering and Management Pune")
            #     value1 = 'Indira College of Engineering and Management Pune'
            
            # elif result[0]=="TSSMS's Pd Vasantdada Patil Institute of Technology Bavdhan  Pune":
            #     print("TSSMS's Pd Vasantdada Patil Institute of Technology Bavdhan  Pune")
            #     value1 = "TSSMS's Pd Vasantdada Patil Institute of Technology Bavdhan  Pune"
            
            # elif result[0]=='Genba Sopanrao Moze Trust Parvatibai Genba Moze College':
            #     print("Genba Sopanrao Moze Trust Parvatibai Genba Moze College")
            #     value1 = 'Genba Sopanrao Moze Trust Parvatibai Genba Moze College'
            
            # elif result[0]=='Progressive Education Society Modern College of Engineering':
            #     print("Progressive Education Society's Modern College of Engineering")
            #     value1 = 'Progressive Education Society  Modern College of Engineering'
            
            # elif result[0]=='Jaywant Shikshan Prasarak Mandal Rajarshi Shahu College of Engineering Tathawade Pune':
            #     print("Jaywant Shikshan Prasarak Mandal'sRajarshi Shahu College of Engineering Tathawade Pune")
            #     value1 = 'Jaywant Shikshan Prasarak Mandal Rajarshi Shahu College of Engineering Tathawade Pune'
            
            # elif result[0]=='Genba Sopanrao Moze College of Engineering Baner-Balewadi':
            #     print("Genba Sopanrao Moze College of Engineering Baner-Balewadi")
            #     value1 = 'Genba Sopanrao Moze College of Engineering Baner-Balewadi'
            
            # elif result[0]=="JSPM'S Jaywantrao Sawant College of EngineeringPune":
            #     print("JSPM'S Jaywantrao Sawant College of EngineeringPune")
            #     value1 = "JSPM'S Jaywantrao Sawant College of EngineeringPune"

            # elif result[0]=='MIT Academy of EngineeringAlandi Pune':
            #     print("MIT Academy of EngineeringAlandi Pune")
            #     value1 = 'MIT Academy of EngineeringAlandi Pune'

            # elif result[0]=='Pimpri Chinchwad Education Trust Pimpri Chinchwad College of Engineering Pune':
            #     print("Pimpri Chinchwad Education Trust Pimpri Chinchwad College of Engineering Pune")
            #     value1 = 'Pimpri Chinchwad Education Trust Pimpri Chinchwad College of Engineering Pune'

            # elif result[0]=='Sinhgad College of Engineering Vadgaon (BK) Pune':
            #     print("Sinhgad College of Engineering Vadgaon (BK) Pune")
            #     value1 = 'Sinhgad College of Engineering Vadgaon (BK) Pune'

            # elif result[0]=='Indira College of Engineering and Management Pune':
            #     print("Indira College of Engineering and Management Pune")
            #     value1 = 'Indira College of Engineering and Management Pune'

            # elif result1=="Pune District Education Association's College of Engineering Pune":
            #     print("Pune District Education Association's College of Engineering Pune")
            #     value1 = 'Pune District Education Association College of Engineering Pune'
            #     print("value1: ",value1)

            # else:
            #     print("Dr D Y Patil Unitech Society's Dr D Y Patil Institute of Technology Pimpri Pune")
            #     value1 = 'Dr D Y Patil Unitech Society Dr D Y Patil Institute of Technology Pimpri Pune'
            
                
            

            #label4 = tk.Label(root,text ="Normal Speech",width=20,height=2,bg='#FF3C3C',fg='black',font=("Tempus Sanc ITC",25))
            #label4.place(x=450,y=550)
    
        return render(request,'result.html',  {
                      'ans': value1,
                      'matching_data':matching_data,
                      'category_upper': category_upper,
                      'department_upper': department_upper,
                    #   'percentile': percentile,
                    #   'college_name' : college_name ,                    
                      'title': 'College Recommendation using Machine Learning',
                      'active': 'btn btn-success peach-gradient text-white',
                      #'no_colleges_found': True,
                      
                  })
    
