from datetime import date
from tkinter import*
import math,random
from tkinter import messagebox
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("750x500+500+120")
        self.root.title("Age Calculator")
        bg_color="#074466"
        title=Label(root,text="*AGE CALCULATOR*",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        
        self.d100=StringVar()
        self.m100=StringVar()
        self.y100=StringVar()
        self.d1000=IntVar()
        self.m1000=IntVar()
        self.y1000=IntVar()
        self.d=IntVar()
        self.d1=IntVar()
        self.d2=IntVar()
        self.d3=IntVar()
        self.d4=IntVar()
        self.d5=IntVar()
        self.d6=IntVar()
        self.d7=IntVar()
        self.d8=IntVar()
        self.m=IntVar()
        self.m1=IntVar()
        self.m2=IntVar()
        self.m3=IntVar()
        self.m4=IntVar()
        self.m5=IntVar()
        self.m6=IntVar()
        self.m7=IntVar()
        self.m8=IntVar()
        self.m9=IntVar()
        self.m=IntVar()
        self.m10=IntVar()
        self.m11=IntVar()
        self.m12=IntVar()
        self.y=IntVar()
        self.y1=IntVar()
        self.y2=IntVar()
        self.y3=IntVar()
        self.y4=IntVar()
        self.y5=IntVar()
        self.y6=IntVar()
        self.y7=IntVar()
        self.y8=IntVar()
        self.y9=IntVar()
        #self.my_date=StringVar()
        
        F1=LabelFrame(self.root,bd=15,relief=GROOVE,font=("times new roman",15,"bold"),fg="gold",bg="#074466")
        F1.place(x=0,y=100,relwidth=1,height=500)
        
        day=Label(F1,text="Enter your birth day",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=5,pady=5,sticky="w")
        day1=Entry(F1,width=5,textvariable=self.d100,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)
        
        month=Label(F1,text="month",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=3,padx=5,pady=5,sticky="w")
        month1=Entry(F1,width=5,textvariable=self.m100,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=4,padx=5,pady=5)
        
        year=Label(F1,text="year",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=5,padx=5,pady=5,sticky="w")
        year1=Entry(F1,width=5,textvariable=self.y100,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=6,padx=5,pady=5)

        bill_btn=Button(F1,text="CALCULATE",command=self.calculator,width=15,bd=7,font="aral 12 bold").grid(row=1,column=0,padx=5,pady=5,sticky="w")
        
        fat_lbl=Label(F1,text="Your age day",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=5,pady=5,sticky="w")
        fat_text=Entry(F1,width=10,textvariable=self.d1000,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=5,pady=5)

        fat_lbl=Label(F1,text="Your age month",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=5,column=0,padx=5,pady=5,sticky="w")
        fat_text=Entry(F1,width=10,textvariable=self.m1000,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=5,pady=5)

        fat_lbl=Label(F1,text="Your age year",font=("times new roman",16,"bold"),bg=bg_color,fg="lightgreen").grid(row=6,column=0,padx=5,pady=5,sticky="w")
        fat_text=Entry(F1,width=10,textvariable=self.y1000,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=5,pady=5)
        
    def calculator(self):
        self.my_date=date.today()
        print("Date:",self.my_date)

        print("Year:",self.my_date.year)
        print("month:",self.my_date.month)
        print("day",self.my_date.day)

        print("Birth Day!")
        self.d.set(int(self.d100.get()))
        self.m.set(int(self.m100.get()))
        self.y.set(int(self.y100.get()))

        #self.d1000.set(int(self.d8.get()))
        #self.m1000.set(int(self.m12.get()))
        #self.y1000.set(int(self.y10.get()))
        #self.d1000={self.d7.get()}
        #self.m1000.set(str(self.m10.get()))
        #self.y1000.set(str(self.y9.get()))
        #d1=my_date.day-d
        #m1=my_date.month-m
        #y1=my_date.year-y
        #print(d1,"/",m1,"/",y1)
        #self.d1000.set(self.)
        #self.m1000.set(self.)
        #self.y1000.set(self.)

        if self.my_date.day<self.d.get() and self.my_date.month<=self.m.get():
            print("if")
            self.d2=self.my_date.day+31
            self.d3=self.d2-self.d.get()
            print("date:",self.d1000.set(self.d3)) 
            self.m2=self.my_date.month-1
            if self.my_date.month>=self.m2:
                print("if madhe if")
                self.m3=self.m2+12
                self.m4=self.m3-self.m.get()
                print("month:",self.m1000.set(self.m4))
                self.y2=self.my_date.year-1
                self.y3=self.y2-self.y.get()
                print("year:",self.y1000.set(self.y3))
                print(self.d3,"/",self.m4,"/",self.y3)
        elif self.my_date.day>=self.d.get() and self.my_date.month>=self.m.get():
            print("1)elif")
            self.d4=self.my_date.day-self.d.get()
            print("date:",self.d1000.set(self.d4))
            self.m5=self.my_date.month-self.m.get()
            print("month:",self.m1000.set(self.m5))
            self.y4=self.my_date.year-self.y.get()
            print("year:",self.y1000.set(self.y4))
            print(self.d4,"/",self.m5,"/",self.y4)       
        elif self.my_date.day>=self.d.get() and self.my_date.month<self.m.get():
            print("2)elif")
            self.d5=self.my_date.day-self.d.get()
            print("date:",self.d1000.set(self.d5))
            self.m5=self.my_date.month+12
            self.m6=self.m5-self.m.get()
            print("month:",self.m1000.set(self.m6))
            self.y5=self.my_date.year-1
            self.y6=self.y5-self.y.get()
            print("year:",self.y1000.set(self.y6))
            print(self.d5,"/",self.m6,"/",self.y6)
        elif self.my_date.day<self.d.get() and self.my_date.month>=self.m.get():
            print("3)elif")
            self.d6=self.my_date.day+31
            self.d7=self.d6-self.d.get()
            print("date:",self.d1000.set(self.d7))
            self.m7=self.my_date.month-1
            #m11=my_date.month-
            if self.m7<self.m.get():
                print("elif madhe if")
                self.m8=self.m7+12
                self.m9=self.m8-self.m.get()
                print("month:",self.m1000.set(self.m9))
                self.y7=self.my_date.year-1
                self.y8=self.y7-self.y.get()
                print("year:",self.y1000.set(self.y8)) 
                print(self.d7,"/",self.m9,"/",self.y8)
            elif self.m7>=self.m.get():
                print("elif madhe if madhe elif")
                self.m10=self.m7-self.m.get()
                print("month:",self.m1000.set(self.m10))
                self.y9=self.my_date.year-self.y.get()
                print("year:",self.y1000.set(self.y9))
                print(self.d7,"/",self.m10,"/",self.y9)
        elif self.my_date.day==self.d.get() and self.my_date.month==self.m.get():
            print("4)elif")
            self.d8=self.my_date.day-self.d.get()
            print("date:",self.d1000.set(self.d8))
            self.m12=self.my_date.month-self.m.get()
            print("month:",self.m1000.set(self.m12))
            self.y10=self.my_date.year-self.y.get()
            print("year:",self.y1000.set(self.y10))
            print(self.d8,"/",self.m12,"/",self.y10)
root=Tk() 
obj = Bill_App(root)
root.mainloop()
