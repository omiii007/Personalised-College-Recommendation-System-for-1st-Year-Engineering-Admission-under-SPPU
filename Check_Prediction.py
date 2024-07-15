from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("800x850+250+5")
    root.title("Employee Turnover Prediction")
    root.configure(background="LightSkyBlue")
    
    Category = tk.StringVar()
    department = tk.StringVar()
    Year = tk.IntVar()
    MHT_CET_Percentile = tk.IntVar()
    
    
    #===================================================================================================================



    def Detect():
        e1=Category.get()
        if e1=="OPEN":
            e1=0
        elif e1=="OBC":
            e1=1
        
        
        elif e1=="NT 2 (NT-C)":
              e1=3
        elif e1=="NT 1 (NT-B)":
              e1=4
        
        elif e1=="SC":
             e1=5
        elif e1=="NT 3 (NT-D)":
             e1=6
        
        else:    
             e1=7
        
        print(e1)
        
        e2=department.get()
        if e2=="Computer Engineering":
            e2=0
        elif e2=="Civil Engineering":
            e2=1
        elif e2=="Mechanical Engineering":
            e2=2
        else:    
             e2=3
        print(e2)
        
        e3=Year.get()
        print(e3)
        
        e4=MHT_CET_Percentile.get()
        print(e4)
        
    # def listToString(s): 
        
    #     # initialize an empty string
    #     str1 = "" 
        
    #     # traverse in the string  
    #     for ele in s: 
    #         str1 = ele  
        
    #     # return string  
    #     return str1 
      
#########################################################################################
        
        from joblib import dump , load
        a1=load('E:/College Recommendation System/DT.joblib')
        v= a1.predict([[e1, e2, e3, e4]])
        print(v)
        
        if v[0]=="DrDYPatil College Of Engineering and InnovationTalegaon":
            print("DrDYPatil College Of Engineering and InnovationTalegaon")
            yes = tk.Label(root,text="DrDYPatil College Of Engineering \n and InnovationTalegaon",background="red",foreground="white",font=('times', 20, ' bold '),width=40)
            yes.place(x=300,y=450) 
            
        if v[0]=="JSPM's Imperial College of Engineering and Research Wagholi Pune":
              print("JSPM's Imperial College of Engineering and Research Wagholi Pune")
              yes = tk.Label(root,text="JSPM's Imperial College of \n Engineering and Research Wagholi Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
              yes.place(x=300,y=450)
              
        if v[0]=="Indira College of Engineering and Management Pune":
              print("Indira College of Engineering and Management Pune")
              yes = tk.Label(root,text="Indira College of Engineering \n and Management Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
              yes.place(x=300,y=450)
              
        
        if v[0]=="TSSMS's Pd Vasantdada Patil Institute of Technology Bavdhan  Pune ":
             print("TSSMS's Pd Vasantdada Patil Institute of Technology Bavdhan  Pune ")
             yes = tk.Label(root,text="TSSMS's Pd Vasantdada Patil Institute \n of Technology Bavdhan  Pune ",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
             yes.place(x=300,y=450)
             
        if v[0]=="Genba Sopanrao Moze Trust Parvatibai Genba Moze College ":
             print("Genba Sopanrao Moze Trust Parvatibai Genba Moze College ")
             yes = tk.Label(root,text="Genba Sopanrao Moze Trust \n Parvatibai Genba Moze College ",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
             yes.place(x=300,y=450)
              
    
        if v[0]=="Progressive Education Society's Modern College of Engineering":
            print("Progressive Education Society's Modern College of Engineering")
            yes = tk.Label(root,text="Progressive Education Society's \n Modern College of Engineering",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
            yes.place(x=300,y=450)
            
            
        if v[0]=="Jaywant Shikshan Prasarak Mandal'sRajarshi Shahu College of Engineering Tathawade Pune":
            print("Jaywant Shikshan Prasarak Mandal'sRajarshi Shahu College of Engineering Tathawade Pune")
            yes = tk.Label(root,text="Jaywant Shikshan Prasarak Mandal'sRajarshi \n Shahu College of Engineering Tathawade Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
            yes.place(x=300,y=450)
            
        if v[0]=="Genba Sopanrao Moze College of Engineering Baner-Balewadi":
                print("Genba Sopanrao Moze College of Engineering Baner-Balewadi")
                yes = tk.Label(root,text="Genba Sopanrao Moze College of \n Engineering Baner-Balewadi",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
                yes.place(x=300,y=450)
                
        if v[0]=="JSPM'S Jaywantrao Sawant College of EngineeringPune":
              print("JSPM'S Jaywantrao Sawant College of EngineeringPune")
              yes = tk.Label(root,text="JSPM'S Jaywantrao Sawant College \n of EngineeringPune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
              yes.place(x=300,y=450)
              
                
        if v[0]=="MIT Academy of EngineeringAlandi Pune":
              print("MIT Academy of EngineeringAlandi Pune")
              yes = tk.Label(root,text="MIT Academy of EngineeringAlandi Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
              yes.place(x=300,y=450)
              
        if v[0]==" Pimpri Chinchwad Education Trust Pimpri Chinchwad College of Engineering Pune":
                print(" Pimpri Chinchwad Education Trust Pimpri Chinchwad College of Engineering Pune")
                yes = tk.Label(root,text=" Pimpri Chinchwad Education Trust\n  Pimpri Chinchwad College of Engineering Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
                yes.place(x=300,y=450)
                
        if v[0]=="Sinhgad College of Engineering Vadgaon (BK) Pune":
                 print("Sinhgad College of Engineering Vadgaon (BK) Pune")
                 yes = tk.Label(root,text="Sinhgad College of Engineering \n Vadgaon (BK) Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
                 yes.place(x=300,y=450)
                 
        if v[0]=="Indira College of Engineering and Management Pune":
                 print("Indira College of Engineering and Management Pune")
                 yes = tk.Label(root,text="Indira College of Engineering \n and Management Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
                 yes.place(x=300,y=450)
                 
        if v[0]=="Pune District Education Association's College of Engineering Pune":
                   print("Pune District Education Association's College of Engineering Pune")
                   yes = tk.Label(root,text="Pune District Education Association's \n College of Engineering Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
                   yes.place(x=300,y=450)
                   
        if v[0]=="Dr D Y Patil Unitech Society's Dr D Y Patil Institute of Technology Pimpri Pune":
                   print("Dr D Y Patil Unitech Society's Dr D Y Patil Institute of Technology Pimpri Pune")
                   yes = tk.Label(root,text="Dr D Y Patil Unitech Society's Dr D Y Patil \n Institute of Technology Pimpri Pune",background="red",foreground="white",font=('times', 20, ' bold '),width=35)
                   yes.place(x=300,y=450)

       
            

           
    l1=tk.Label(root,text="Category",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l1.place(x=5,y=30)
    monthchoosen = ttk.Combobox(root, width = 27, textvariable = Category)

   # Adding combobox drop down list
    monthchoosen['values'] = ('OPEN',
   						'OBC',
   					
   					' NT 1 (NT-B)',
   						' NT 2 (NT-C)','NT 3 (NT-D)',
   						'SC')
    monthchoosen.place(x=500,y=50)
   #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()

    l2=tk.Label(root,text="department",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l2.place(x=5,y=90)
    monthchoosen = ttk.Combobox(root, width = 27, textvariable = department)

   # Adding combobox drop down list
    monthchoosen['values'] = ('Computer Engineering',
   						'Civil Engineering',
   						'Mechanical Engineering',
   						'Information Technology')
   						
    monthchoosen.place(x=500,y=100)
   #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
    l3=tk.Label(root,text="Year",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l3.place(x=5,y=150)
    Year=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Year)
    Year.place(x=500,y=150)
    
    l4=tk.Label(root,text="MHT_CET_Percentile",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l4.place(x=5,y=200)
    MHT_CET_Percentile=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=MHT_CET_Percentile)
    MHT_CET_Percentile.place(x=500,y=200)
    
    button1 = tk.Button(root, foreground="white", background="red",text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=600)


    root.mainloop()

Train()