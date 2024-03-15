# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:24:21 2023

@author: Student
"""

#class produkt:
#    ilosc = 0
#    def ustaw_ilosc(self, ilosc):
#        self.ilosc = ilosc
        
#class przedmiot1(produkt):
#    opis = 'przedmiot1'
    
#p = przedmiot1()
#p.ustaw_ilosc(11)
#print(p.ilosc)
#print(p.opis)

#class produkt:
#    ilosc = 0
#    def __init__(self):
#        self.ilosc = 111
#        def ustaw_ilosc(self, ilosc):
#            self.ilosc = ilosc
#class przedmiot1(produkt):
#    def __init__(self):
#        produkt.__init__(self)
#        opis = 'przedmiot1'

#p = przedmiot1()
#print(p.ilosc)
#print =(p.opis)

#from tkinter import *

#class App:
#    def __init__(self,master):
#        frame = Frame(master, width=600, height=300)
#        frame.pack()
        
#        Label(frame,text='Wpisz liczbe: ').grid(row=0,column=0)
#        self.first_var=DoubleVar()
#        Entry(frame,textvariable=self.first_var).grid(row=0,column=1)
        

#        button=Button(frame,text='Wyswietl liczbe',command=self.display)
#        button.grid(row=3,column = 0)


#        self.result_addition=DoubleVar()
#        Label(frame,textvariable=self.result_addition).grid(row=2,column=0)
        
#    def display(self):
#        a=self.first_var.get()
#        self.result_addition.set(a)
        

#root = Tk()
#root.wm_title('Wyswietlacz liczb')
#app=App(root)
#root.mainloop()

from tkinter import*

class App:
    def __init__(self,master):
        frame=Frame(master, width=400, height=400)
        frame.pack()
        
        Label(frame,text='wpisz liczbe 1: ').grid(row=0,column=0)
        self.first_var=DoubleVar()
        Entry(frame,textvariable=self.first_var).grid(row=0,column=1)
    
        Label(frame,text='wpisz liczbe 2: ').grid(row=1,column=0)
        self.second_var=DoubleVar()
        Entry(frame,textvariable=self.second_var).grid(row=1,column=1)   
    

    
        self.wynik=DoubleVar()
        Label(frame,text='wynik: ').grid(row=3,column=0)
        Label(frame,textvariable=self.wynik).grid(row=3,column=1)
        
        button_suma= Button(frame,text='suma',command=self.suma)
        button_suma.grid(row=4,column = 0)
        
        button_roznica= Button(frame,text='roznica',command=self.roznica)
        button_roznica.grid(row=4,column = 1)
        
        button_iloczyn= Button(frame,text='iloczyn',command=self.iloczyn)
        button_iloczyn.grid(row=5,column =0)
        
        button_iloraz= Button(frame,text='iloraz',command=self.iloraz)
        button_iloraz.grid(row=5,column = 1)
        
    def suma(self):
        
        first=self.first_var.get() 
        second=self.second_var.get()
        self.wynik.set(first+second)
        
    def roznica(self):
        
        first=self.first_var.get()
        second=self.second_var.get()
        self.wynik.set(first-second)
        
    def iloczyn(self):
        
        first=self.first_var.get() 
        second=self.second_var.get()
        self.wynik.set(first*second)
        
    def iloraz(self):
        
        first=self.first_var.get()
        second=self.second_var.get()
        self.wynik.set(first/second)
        

        
root=Tk()
root.wm_title('Wyswietlacz wynikow')
app=App(root)
root.mainloop()
        