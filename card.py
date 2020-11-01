# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:33:36 2020

@author: Hp
"""
from tkinter import*
import random


def confirmed():
    messagebox.showinfo("Confirmation", "Booking successful with \n Ticket No. "+str(random.randint(111111,999999)))

def cards():
    sc1= Tk()
    sc1.geometry("1800x600")
    sc1.configure(bg="white")
    t1=StringVar()
    t2=StringVar()
    t3=StringVar()
    t4=StringVar()
    t5=StringVar()
    Label(sc1,text ="BUS",font=("arial", 20),fg="red",bg="white",height=2,width=50,bd=7).place(x=330,y=0)
    Label(sc1,text ="YATRI",font=("arial", 20),fg="blue",bg="white",height=2,width=5).place(x=770,y=4)
    Label(sc1,text ="Payment Options",font=("arial", 40),fg="white",bg="blue",height=2,width=20,bd=6).place(x=450,y=52)
    Label(sc1,text ="Card Number",font=("arial", 20),fg="blue",bg="white",height=2,width=50,bd=7).place(x=150,y=200)
    Label(sc1,text ="Month",font=("arial", 20),fg="blue",bg="white",height=2,width=50).place(x=120,y=320)
    Label(sc1,text ="Year",font=("arial", 20),fg="blue",bg="white",height=2,width=10).place(x=625,y=320)
    Label(sc1,text ="CVV",font=("arial", 20),fg="blue",bg="white",height=2,width=10).place(x=810,y=320)
    Label(sc1,text ="Cardholder name",font=("arial", 20),fg="blue",bg="white",height=2,width=30).place(x=340,y=400)
    tt1=Entry(sc1,bd=5,font=("Arial", 30),bg="honeydew",textvariable=t1)
    tt1.place(x=480,y=280)
    tt2=Entry(sc1,bd=2,font=("Arial",10),bg="honeydew",textvariable=t2)
    tt2.place(x=480,y=370)
    tt3=Entry(sc1,bd=2,font=("Arial",10),bg="honeydew",textvariable=t3)
    tt3.place(x=630,y=370)
    tt4=Entry(sc1,bd=2,font=("Arial",10),bg="honeydew",textvariable=t4)
    tt4.place(x=780,y=370)
    tt5=Entry(sc1,bd=2,font=("Arial",20),bg="honeydew",textvariable=t5)
    tt5.place(x=480,y=450)
    B1=Button(sc1,text="PAY AND CONFIRM BOOKING",height = 2, width = 40,font=("ARIAL",15),fg="white",bg="black",command=confirmed)
    B1.place(x=470,y=500)
    sc1.mainloop()