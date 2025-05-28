from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC  # Import the SVM classifier
from sklearn.metrics import classification_report, accuracy_score
from joblib import dump
from sklearn.ensemble import RandomForestClassifier 
root = tk.Tk()
root.title("Credit Card Fraud Detection")
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++
image2 = Image.open('4.jpg')
image2 = image2.resize((w,h))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)




lbl = tk.Label(root, text="Credit Card Fraud Detection", font=('times', 28,' bold italic'), height=1, width=70,bg="darkblue",fg="White")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv("D:/23 Protech/100% code/Credit Card Fraud Detection/credit card fraud-new/training.csv")



data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv("D:/23 Protech/100% code/Credit Card Fraud Detection/credit card fraud-new/training.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['step'] = le.fit_transform(data['step'])
    
    data['Types'] = le.fit_transform(data['Types'])
    
    data['amount'] = le.fit_transform(data['amount'])
    
    data['oldbalanceOrg'] = le.fit_transform(data['oldbalanceOrg'])

    data['newbalanceOrig'] = le.fit_transform(data['newbalanceOrig'])
    
    data['oldbalanceDest'] = le.fit_transform(data['oldbalanceDest'])
    
    data['newbalanceDest'] = le.fit_transform(data['newbalanceDest'])
    
   
    
  

    """Feature Selection => Manual"""
    x = data.drop(['isFlaggedFraud'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['isFlaggedFraud']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=350, y=80)


def Model_Training():
    data = pd.read_csv("D:/23 Protech/100% code/Credit Card Fraud Detection/credit card fraud-new/training.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['step'] = le.fit_transform(data['step'])
    
    data['Types'] = le.fit_transform(data['Types'])
    
    data['amount'] = le.fit_transform(data['amount'])
    
    data['oldbalanceOrg'] = le.fit_transform(data['oldbalanceOrg'])

    data['newbalanceOrig'] = le.fit_transform(data['newbalanceOrig'])
    
    data['oldbalanceDest'] = le.fit_transform(data['oldbalanceDest'])
    
    data['newbalanceDest'] = le.fit_transform(data['newbalanceDest'])
    

    

    """Feature Selection => Manual"""
    x = data.drop(['isFlaggedFraud'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['isFlaggedFraud']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=999)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)
    
    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=405,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as model.joblib",width=45,height=3,bg='white',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=405,y=420)
    from joblib import dump
    dump (svcclassifier,"model.joblib")
    print("Model saved as model.joblib")

def Model_Training1():
    data = pd.read_csv("D:/23 Protech/100% code/Credit Card Fraud Detection/credit card fraud-new/training.csv")
    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['step'] = le.fit_transform(data['step'])
    data['Types'] = le.fit_transform(data['Types'])
    data['amount'] = le.fit_transform(data['amount'])
    data['oldbalanceOrg'] = le.fit_transform(data['oldbalanceOrg'])
    data['newbalanceOrig'] = le.fit_transform(data['newbalanceOrig'])
    data['oldbalanceDest'] = le.fit_transform(data['oldbalanceDest'])
    data['newbalanceDest'] = le.fit_transform(data['newbalanceDest'])

    """Feature Selection => Manual"""
    x = data.drop(['isFlaggedFraud'], axis=1)
    y = data['isFlaggedFraud']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=999)

    # Replace Decision Tree Classifier with SVM
    svcclassifier = SVC(kernel='linear')  # You can choose different kernels like 'linear', 'rbf', etc.
    svcclassifier.fit(x_train, y_train)
    
    y_pred = svcclassifier.predict(x_test)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = accuracy_score(y_test, y_pred) * 100
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=10, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=405, y=200)

    label5 = tk.Label(root, text="Accuracy : " + str(ACC) + "%\nModel saved as modelsvm.joblib", width=45, height=3,
                      bg='white', fg='black', font=("Tempus Sanc ITC", 14))
    label5.place(x=405, y=420)

    dump(svcclassifier, "modelsvm.joblib")
    print("Model saved as modelsvm.joblib")
    
def Model_Training2():
    data = pd.read_csv("training.csv")
    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['step'] = le.fit_transform(data['step'])
    data['Types'] = le.fit_transform(data['Types'])
    data['amount'] = le.fit_transform(data['amount'])
    data['oldbalanceOrg'] = le.fit_transform(data['oldbalanceOrg'])
    data['newbalanceOrig'] = le.fit_transform(data['newbalanceOrig'])
    data['oldbalanceDest'] = le.fit_transform(data['oldbalanceDest'])
    data['newbalanceDest'] = le.fit_transform(data['newbalanceDest'])

    """Feature Selection => Manual"""
    x = data.drop(['isFlaggedFraud'], axis=1)
    y = data['isFlaggedFraud']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=999)

    # Replace Decision Tree Classifier with Random Forest Classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=999)  # You can adjust the number of trees (n_estimators)
    rf_classifier.fit(x_train, y_train)
    
    y_pred = rf_classifier.predict(x_test)

    print("=" * 40)
    print("==========")
    print("Classification Report : ", classification_report(y_test, y_pred))
    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = accuracy_score(y_test, y_pred) * 100
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=10, bg='khaki', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=405, y=200)

    label5 = tk.Label(root, text="Accuracy : " + str(ACC) + "%\nModel saved as modelRF.joblib", width=45, height=3,
                      bg='white', fg='black', font=("Tempus Sanc ITC", 14))
    label5.place(x=405, y=420)

    dump(rf_classifier, "modelRF.joblib")
    print("Model saved as modelRF.joblib")

# Assuming you have a tkinter root window defined here
# root = tk.Tk()
# Model_Training()
# root.mainloop()

def call_file():
    from subprocess import call
    call(["python","Check_Prediction.py"])


def window():
    root.destroy()

# button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# button2.place(x=5, y=90)

# button3 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=170)
button3 = tk.Button(root, foreground="black", background="#00BFFF", font=("times", 14, "bold"),
                    text="SVM Algorithm", command=Model_Training1, width=15, height=2)
button3.place(x=50, y=150)

button2 = tk.Button(root, foreground="black", background="white", font=("times", 14, "bold"),
                    text="RF Algorithm", command=Model_Training2, width=15, height=2)
button2.place(x=50, y=250)

button4 = tk.Button(root, foreground="black", background="#00BFFF", font=("times", 14, "bold"),
                    text="DT Algorithm", command=Model_Training, width=15, height=2)
button4.place(x=50, y=350)

exit1 = tk.Button(root, text="Prediction", command=call_file, width=15, height=2, font=('times', 15, ' bold '),bg="white",fg="black")
exit1.place(x=50, y=450)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=50, y=550)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''