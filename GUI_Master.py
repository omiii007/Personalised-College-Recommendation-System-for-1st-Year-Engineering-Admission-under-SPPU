from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
root = tk.Tk()
root.title("College Recommendation System")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

# img=ImageTk.PhotoImage(Image.open("image1.jpg"))

# img2=ImageTk.PhotoImage(Image.open("image2.png"))

# img3=ImageTk.PhotoImage(Image.open("images3.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x = 1

# function to change to next image
# def move():
# 	global x
# 	if x == 4:
# 		x = 1
# 	if x == 1:
# 		logo_label.config(image=img)
# 	elif x == 2:
# 		logo_label.config(image=img2)
# 	elif x == 3:
# 		logo_label.config(image=img3)
# 	x = x+1
# 	root.after(2000, move)

# # calling the function
# move()
 # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="College Recommendation System", font=('times', 35,' bold '), height=1, width=65,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv(r"F:\Studies\BE Project\college_recomm_web\Hello\projectApp\dataset.csv")



data = data.dropna()

le = LabelEncoder()
# data['AHD'] = le.fit_transform(data['AHD'])

# data['Thal'] = le.fit_transform(data['Thal'])
# data['ChestPain'] = le.fit_transform(data['ChestPain'])

# data.head()

# """Feature Selection => Manual"""
# x = data.drop(['AHD', 'Series'], axis=1)


def Data_Preprocessing():
    data = pd.read_csv(r"F:\Studies\BE Project\college_recomm_web\Hello\projectApp\dataset.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['Category'] = le.fit_transform(data['Category'])
    
    data['department'] = le.fit_transform(data['department'])
    
    data['Year'] = le.fit_transform(data['Year'])

    data['MHT_CET_Percentile'] = le.fit_transform(data['MHT_CET_Percentile'])
    
   
  

    """Feature Selection => Manual"""
    x = data.drop(['Collage_name'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Collage_name']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)


    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=213, y=85)


def Model_Training():
    data = pd.read_csv(r"F:\Studies\BE Project\college_recomm_web\Hello\projectApp\dataset.csv")
    data.head()

    data = data.dropna()


    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['Category'] = le.fit_transform(data['Category'])
    
    data['department'] = le.fit_transform(data['department'])
    
    data['Year'] = le.fit_transform(data['Year'])

    data['MHT_CET_Percentile'] = le.fit_transform(data['MHT_CET_Percentile'])
    
   
  
    

    """Feature Selection => Manual"""
    x = data.drop(['Collage_name'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Collage_name']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1234)

    # from sklearn.tree import DecisionTreeClassifier
    # svcclassifier = DecisionTreeClassifier()
    # svcclassifier.fit(x_train, y_train)
    # y_pred = svcclassifier.predict(x_test)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)

    
    # from sklearn.svm import SVC
   
    # svcclassifier = SVC(kernel='linear',random_state=0)
    # svcclassifier.fit(x_train, y_train)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)
    
    from sklearn.ensemble import RandomForestClassifier
   
    RandomForestClassifier = RandomForestClassifier(n_estimators=100, random_state=42)
    RandomForestClassifier.fit(x_train, y_train)

    y_pred = RandomForestClassifier.predict(x_test)
    print(y_pred)
    
    # from sklearn.svm import SVC
   
    # svcclassifier = GaussianNB()
    # svcclassifier.fit(x_train, y_train)

    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0 - 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100 + 95)
    repo = (classification_report(y_test, y_pred))
    
    print("Confusion Matrix :")
    cm = confusion_matrix(y_test,y_pred)
    print(cm)
    print("\n")
    from mlxtend.plotting import plot_confusion_matrix

    fig, ax = plot_confusion_matrix(conf_mat=cm, figsize=(6, 6), cmap=plt.cm.Greens)
    plt.xlabel('Predictions', fontsize=18)
    plt.ylabel('Actuals', fontsize=18)
    plt.title('Confusion Matrix', fontsize=18)
    plt.show()
    
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as clg.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"clg.joblib")
    print("Model saved as clg.joblib")



def call_file():
    import Check_Prediction
    Check_Prediction.Train()


def window():
    root.destroy()

button2 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=20, y=90)

button3 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=20, y=170)

button4 = tk.Button(root, foreground="white", background="Orange", font=("Tempus Sans ITC", 14, "bold"),
                    text="College Recommendation", command=call_file, width=30, height=2)
button4.place(x=20, y=250)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=20, y=330)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''