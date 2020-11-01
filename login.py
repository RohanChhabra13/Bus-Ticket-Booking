from tkinter import *

from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
from mainpage import*

def check():
    cn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='ticket_booking')
    cur=cn.cursor()
    st="select * from login where email='{}' and passwd='{}'".format(t1.get(),t2.get())
    cur.execute(st)
    x=cur.fetchall()
    if len(x)==1:
        messagebox.showinfo("Say Hello", "login successful")
        sys()
    else:
        messagebox.showinfo("Say Hello", "invalid username or password")

    cn.close()

def login(sc):
    global t1
    global t2
    t1=StringVar()
    t2=StringVar()
    sc1= Toplevel(sc)
    sc1.geometry("4096x2160")
    sc1.configure(bg="white")
    Label(sc1,text ="BUS",font=("arial", 20),fg="red",bg="white",height=2,width=50,bd=7).place(x=330,y=0)
    Label(sc1,text ="YATRI",font=("arial", 20),fg="blue",bg="white",height=2,width=5).place(x=770,y=4)
    Label(sc1,text ="LOGIN",font=("arial", 40),fg="white",bg="blue",height=2,width=50,bd=6).place(x=0,y=52)
    Label(sc1,text ="EMAIL",font=("arial", 20),fg="black",bg="white").place(x=550,y=300)
    Label(sc1,text="Need Assistence? Contact us",font=("arial",10),fg="black",bg="white").place(x=500,y=700)
    Label(sc1,text="voyagerbusservices@gmail.com",font=("arial",10),fg="black",bg="white").place(x=500,y=730)    
    tt1=Entry(sc1,bg="honeydew",fg="black",font=("Arial", 14),textvariable=t1)
    tt1.place(x=700,y=310)
    Label(sc1,text ="PASSWORD",font=("arial", 20),fg="black",bg="white").place(x=500,y=390)
    tt2=Entry(sc1,show='*',bg="honeydew",font=("Arial", 14),textvariable=t2)
    tt2.place(x=700,y=400)
    b1=Button(sc1,text ="Login",height = 2, width= 30,fg="white",bg="black",font=("Arial", 14),command=lambda:check())
    b1.place(x=600,y=500)
    sc1.mainloop()