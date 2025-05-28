import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk



##############################################+=============================================================
root = tk.Tk()
root.configure(background="black")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Credit Fraud Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('1.png')
image2 = image2.resize((w,h))

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)


#
lbl = tk.Label(root, text="Credit Fraud Detection using Machine Learning", font=('times',28,' bold '),bg="blue",fg="white",width='65')
lbl.place(x=0, y=0)









def log():
#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    from subprocess import call
    call(["python","login.py"])
    #root.destroy()
    
def reg():
    from subprocess import call
    call(["python","registration.py"])
    #root.destroy()
    
def window():
  root.destroy()
  


#####################################################################################################################

button1 = tk.Button( text="Login", command=log, width=15, height=1,font=('times', 15, ' bold '), bg="blue", fg="white")
button1.place(x=800, y=50)

button2 = tk.Button( text="Registration",command=reg,width=15, height=1,font=('times', 15, ' bold '), bg="green", fg="white")
button2.place(x=1000, y=50)

button3 = tk.Button( text="Exit",command=window,width=15, height=1,font=('times',15, ' bold '), bg="red", fg="white")
button3.place(x=1200, y=50)





root.mainloop()