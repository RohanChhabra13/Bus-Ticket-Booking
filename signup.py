# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:48:21 2020

@author: Hp
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mainpage import*
from login import*
import mysql.connector
def add():
    cn = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='ticket_booking')
    cur=cn.cursor()
    st="insert into login(firstname,lastname,mobileno,address,city,state,aadharno,email,passwd) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(t1.get(),t2.get(),t3.get(),t4.get(),t5.get(),t6.get(),t7.get(),t8.get(),t9.get())
    cur.execute(st)
    cn.commit()



def signup(sc):
    global t1
    global t2
    global t3
    global t4
    global t5
    global t6
    global t7
    global t8
    global t9
    global t10
    
    t1=StringVar()
    t2=StringVar()
    t3=StringVar()
    t4=StringVar()
    t5=StringVar()
    t6=StringVar()
    t7=StringVar()
    t8=StringVar()
    t9=StringVar()
    t10=StringVar()
    sc1= Toplevel(sc)
    sc1.geometry("4096x2160")
    sc1.configure(bg="white")
    Label(sc1,text ="PASSWORD",font=("arial", 20),fg="black",bg="white").place(x=300,y=600)
    tt9=Entry(sc1,font=("arial",14),textvariable=t9)
    tt9.place(x=500,y=600)
    Label(sc1,text ="BUS",font=("arial", 20),fg="red",bg="white",height=2,width=50,bd=7).place(x=330,y=0)
    Label(sc1,text ="YATRI",font=("arial", 20),fg="blue",bg="white",height=2,width=5).place(x=770,y=4)
    Label(sc1,text ="REGISTER",font=("arial", 40),fg="white",bg="blue",height=2,width=50,bd=6).place(x=0,y=52)
    Label(sc1,text ="EMAIL",font=("arial", 20),fg="black",bg="white").place(x=750,y=500)
    tt2=Entry(sc1,font=("Arial", 14),textvariable=t2)
    tt2.place(x=500,y=500)
    Label(sc1,text="Need Assistence? Contact us",font=("arial",10),fg="black",bg="white").place(x=1300,y=700)
    Label(sc1,text="busyatriservices@gmail.com",font=("arial",10),fg="black",bg="white").place(x=1300,y=730)
    Label(sc1,text="First Name",font=("arial",20),fg="black",bg="white").place(x=350,y=200)
    tt3=Entry(sc1,font=("arial",14),textvariable=t3)
    tt3.place(x=500,y=200)
    Label(sc1,text="Last Name",font=("arial",20),fg="black",bg="white").place(x=750,y=200)
    tt4=Entry(sc1,font=("arial",14),textvariable=t4)
    tt4.place(x=900,y=200)
    Label(sc1,text="Mobile No.",font=("arial",20),fg="black",bg="white").place(x=350,y=300)
    tt5=Entry(sc1,font=("arial",14),textvariable=t5)
    tt5.place(x=500,y=300)
    Label(sc1,text="Address",font=("arial",20),fg="black",bg="white").place(x=755,y=300)
    tt6=Entry(sc1,font=("arial",14),textvariable=t6)
    tt6.place(x=900,y=300)
    Label(sc1,text="City",font=("arial",20),fg="black",bg="white").place(x=370,y=400)
    tt1=Entry(sc1,font=("Arial", 14),textvariable=t1)
    tt1.place(x=500,y=400)
    Label(sc1,text="State",font=("arial",20),fg="black",bg="white").place(x=765,y=400)
    tt7=Entry(sc1,font=("arial",14),textvariable=t7)
    tt7.place(x=900,y=400)
    Label(sc1,text="Aadhar Number",font=("arial",20),fg="black",bg="white").place(x=300,y=500)
    tt8=Entry(sc1,font=("arial",14),textvariable=t8)
    tt8.place(x=900,y=500)
    Label(sc1,text="Referral Code",font=("arial",17),fg="black",bg="white").place(x=750,y=600)
    tt10=Entry(sc1,font=("arial",14),bg="honeydew",textvariable=t10)
    tt10.place(x=900,y=600)
    Label(sc1,text="Use Referral code",font=("arial",10),fg="black",bg="white").place(x=950,y=635)
    Label(sc1,text="To get upto 50% off",font=("arial",10),fg="black",bg="white").place(x=950,y=655)
    B1=Button(sc1,text="Create Account",height = 2, width = 40,font=("ARIAL",15),fg="white",bg="black" ,command=lambda:add())
    B1.place(x=550,y=675)
    B2=Button(sc1,text="Login",height = 1, width = 40,font=("ARIAL",15),fg="white",bg="black" ,command=lambda:login(sc1))
    B2.place(x=550,y=750)
    sc1.mainloop()