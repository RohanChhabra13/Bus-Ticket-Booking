# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:37:27 2020

@author: Hp
"""
from tkinter import*
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
from card import*
from tkcalendar import Calendar,DateEntry
import mysql.connector

def connects():
    global cn
    cn=mysql.connector.connect(user='root',password='root',host='localhost',database='ticket_booking')

def ShowChoice():
    cards()

def search():
    global rad
    rad=StringVar()
    xaxis=525
    yaxis=350
    cur=cn.cursor()
    st="select busno,source,destination,timing,amount from bus where source='{}' and destination='{}'".format(tt1.get(),tt2.get())
    cur.execute(st)
    li=cur.fetchall()
    if len(li)==0:
        if messagebox.showinfo("Problem", "Route Doesn't Exist"):
            w.destroy()
            sys()
    else:
        for i in li:
            print(i)
        for i in li: 
            no,src,des,time,amt=i
            Radiobutton(sc,text="Bus no "+no+" "+src+" "+des+" "+time+" Rs"+amt+" ",padx=20,variable=rad,value=no,height=2,width=30,font=("arial",20),bg="azure3",command=ShowChoice).place(x=xaxis,y=yaxis)        
            yaxis+=75

def sys():
    global sc
    global tt1
    global tt2
    connects()
    sc = Tk()
    sc.geometry("4096x2160")
    sc.configure(bg="white")
    sc.title('BUS YATRI')
    t1=StringVar()
    t2=StringVar()
    cal = DateEntry(sc,width=30,bg="darkblue",fg="white",year=2020,)
    cal.place(x=1110,y=208)
    Label(sc,text ="BUS",font=("arial", 40),fg="red",bg="white").place(x=610,y=0)
    Label(sc,text ="YATRI",font=("arial", 40),fg="blue",bg="white").place(x=720,y=0)
    L2=Label(sc,text="DATE",font=("ARIAL",20),fg="black",bg="white")
    L2.place(x=1030,y=200)
    L3=Label(sc,text="FROM",font=("ARIAL",20),fg="black",bg="white")
    L3.place(x=290,y=200)
    L4=Label(sc,text="DESTINATION",font=("ARIAL",20),fg="black",bg="white")
    L4.place(x=610,y=200)
    
    tt1=Combobox(sc,width=27,textvariable=t1)
    cur=cn.cursor()
    st="select distinct(source) from bus"
    cur.execute(st)
    li=cur.fetchall()
    tt1['values']=(tuple(li))
    #tt1=Entry(sc,bd=5,font=("Arial", 14),textvariable=t1)
    tt1.place(x=377,y=210)
    
    #tt2=Entry(sc,bd=5,font=("Arial", 14),textvariable=t2)
    tt2=Combobox(sc,width=27,textvariable=t2)
    cur=cn.cursor()
    st="select distinct(destination) from bus"
    cur.execute(st)
    li2=cur.fetchall()
    tt2['values']=(tuple(li2))
    tt2.place(x=798,y=210)
    
    B1=Button(sc,text="SEARCH",height = 2, width = 15,font=("ARIAL",15),fg="white",bg="black",command=search)
    B1.place(x=700,y=250)

    labelframe_tk= LabelFrame(sc, text="SUPERIOR CUSTOMER SERVICES",font=("arial",20),bg="honeydew")
    labelframe_tk.pack(padx=550,pady=100,fill="both", expand="no")
    inside = Label(labelframe_tk, text="We put our experience and relationships to",font=("arial,14"))
    inside.pack(padx=0,pady=2)
    inside = Label(labelframe_tk, text="to good use and",font=("arial,14"))
    inside.pack(padx=0,pady=2)
    inside = Label(labelframe_tk, text="are available to solve your travel issues.",font=("arial,14"))
    inside.pack(padx=0,pady=2)
    labelframe_tk.place(x=25,y=550)
    labelframe_t= LabelFrame(sc, text="LOWEST PRICES",font=("arial",20),bg="honeydew")
    labelframe_t.pack(padx=550,pady=100,fill="both", expand="no")
    inside = Label(labelframe_t, text="We always give you",font=("arial,14"))
    inside.pack(padx=5,pady=2)
    inside = Label(labelframe_t, text="the lowest price with the best partner offers.",font=("arial,14"))
    inside.pack(padx=5,pady=2)
    inside = Label(labelframe_t, text="with the best partner offers.",font=("arial,14"))
    inside.pack(padx=5,pady=2)
    labelframe_t.place(x=600,y=550)
    labelframe_k= LabelFrame(sc, text="UNMATCHED BENEFITS",font=("arial",20),bg="honeydew")
    labelframe_k.pack(padx=550,pady=100,fill="both", expand="no")
    inside = Label(labelframe_k, text="We take care of your travel beyond ticketing",font=("arial,14"))
    inside.pack(padx=5,pady=2)
    inside = Label(labelframe_k, text="by providing you",font=("arial,14"))
    inside.pack(padx=5,pady=2)
    inside = Label(labelframe_k, text="with innovative and unique benefits.",font=("arial,14"))
    inside.pack(padx=5,pady=2)
    labelframe_k.place(x=1100,y=550)
    '''  labelframe_a= LabelFrame(sc, text="COVID SAFE BUSES",font=("arial",20),bg="honeydew")
    labelframe_a.pack(padx=550,pady=100,fill="both", expand="no")
    inside = Label(labelframe_a, text="Introducing Safety+",font=("arial,14"))
    inside.pack(padx=0,pady=0)
    inside = Label(labelframe_a, text="1 Sanitized Bus",font=("arial,14"))
    inside.pack(padx=10,pady=10)
    inside = Label(labelframe_a, text="2 Mandatory masks",font=("arial,14"))
    inside.pack(padx=40,pady=10)
    inside = Label(labelframe_a, text="3 Thermal Screening",font=("arial,14"))
    inside.pack(padx=70,pady=10)
    labelframe_a.place(x=500,y=100)'''
    sc.mainloop()   