
from tkinter import*
from login import*
from signup import*
from PIL import ImageTk,Image
sc =Tk()
sc.geometry("4096x2160")
image = Image.open("450833.jpg")
photo = ImageTk.PhotoImage(image)
L = Label(image=photo,height=900,width=1600).place(x=0,y=0)
L1=Label(sc,text="BUS",font=("ARIAL",50),fg="red",bg="white")
L1.place(x=590,y=0)
L1=Label(sc,text="YATRI",font=("ARIAL",50),fg="blue",bg="white")
L1.place(x=730,y=0)
B1=Button(sc,text="Login",height = 2, width = 40,font=("ARIAL",15),fg="white",bg="black" ,command=lambda:login(sc))
B1.place(x=520,y=400)
L2=Label(sc,text="Don't have an account?",font=("ARIAL",20),fg="black",bg="white")
L2.place(x=600,y=600)
B2=Button(sc,text="Signup",height = 2, width = 40,font=("ARIAL",15),fg="white",bg="black",command=lambda:signup(sc))
B2.place(x=520,y=700)
sc.mainloop()
