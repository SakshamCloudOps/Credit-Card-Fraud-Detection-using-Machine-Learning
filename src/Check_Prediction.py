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

    root.geometry("800x850")
    root.title("Credit Fraud Detection")
    root.configure(background="#00BFFF")
    
    step= tk.IntVar()
    Types= tk.StringVar()
    amount = tk.IntVar()
    oldbalanceOrg = tk.IntVar()
    newbalanceOrig= tk.IntVar()
    oldbalanceDest = tk.IntVar()
    newbalanceDest =  tk.IntVar()
   
    
    lbl = tk.Label(root, text="Fraud Detection System", font=('times', 25,' bold '), height=1, width=45,bg="darkolivegreen1",fg="blue")
    lbl.place(x=0, y=0)
    #===================================================================================================================



    def Detect():
        
        
        
        e1=step.get()
        print(e1)
       
        e2=Types.get()
        if e2=="PAYMENT":
            e2=0
        elif e2=="CASH_OUT":
            e2=1
        elif e2=="TRANSFER":
            e2=2
        elif e2=="DEBIT":
            e2=3
        else:    
             e2=4
        print(e2)
        
        e3=amount.get()
        print(e3)
        
        e4=oldbalanceOrg.get()
        print(e4)
        
        e5=newbalanceOrig.get()
        print(e5)
        
        
        e6=oldbalanceDest.get()
        print(e6)
        
        e7=newbalanceDest.get()
        print(e7)
        
           
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('model.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7]])
        print(v)
    
        if v[0]==0:
           print("No Fraud Detected")
           yes = tk.Label(root,text="No Credit Card-Fraud Detected ",background="green",foreground="white",font=('times', 20, ' bold '),width=25)
           yes.place(x=300,y=600)
           
           
        if v[0]==1:
           print("Fraud Detected")
           yes = tk.Label(root,text="Credit Card-Fraud Detected",background="red",foreground="white",font=('times', 20, ' bold '),width=25)
           yes.place(x=260,y=600)

            
    
    l1=tk.Label(root,text="STEP",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=20)
    l1.place(x=45,y=100)
    step=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=step)
    step.place(x=400,y=100)
    
    
    l2=tk.Label(root,text="Type Of Transaction",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=25)
    l2.place(x=5,y=150)
    
   
    monthchoosen = ttk.Combobox(root, width = 25, textvariable = Types)
    # Adding combobox drop down list
    monthchoosen['values'] = (' PAYMENT',
    						' CASH_OUT',
    						' TRANSFER',
                            'CASH_IN')
    monthchoosen.place(x=400,y=150)
    #monthchoosen.grid(column = 1, row = 5)
    monthchoosen.current()
   

    
    l3=tk.Label(root,text="Transaction Amount",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=25)
    l3.place(x=5,y=200)
    amount=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=amount)
    amount.place(x=400,y=200)
    
    l4=tk.Label(root,text="Balance Before Transaction",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=25)
    l4.place(x=5,y=250)
    oldbalanceOrg=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=oldbalanceOrg)
    oldbalanceOrg.place(x=400,y=250)
     
     
    l5=tk.Label(root,text="Balance After Transaction",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=25)
    l5.place(x=5,y=300)
    newbalanceOrig=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=newbalanceOrig)
    newbalanceOrig.place(x=400,y=300)
    
    l6=tk.Label(root,text="Old Transfer Transaction",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=25)
    l6.place(x=5,y=350)
    oldbalanceDest=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=oldbalanceDest)
    oldbalanceDest.place(x=400,y=350)
    
    l7=tk.Label(root,text="New Transfer Transaction",background="#00BFFF",fg='black',font=('times', 20, ' bold '),width=25)
    l7.place(x=5,y=400)
    newbalanceDest=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=newbalanceDest)
    newbalanceDest.place(x=400,y=400)
     
    
      
   
    
    button1 = tk.Button(root, foreground="white", background="GREEN",text="SUBMIT",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=300,y=450)


    root.mainloop()

Train()