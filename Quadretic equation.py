from tkinter import *
import math




root=Tk()
root.title("Quadratic")
root.geometry('200x200')
a_input=Entry(root)
a_input.grid(row=1,column=1)	
b_input=Entry(root)
b_input.grid(row=3,column=1)	
c_input=Entry(root)
c_input.grid(row=5,column=1)	

x='aaa'

a_meseage=Label(root,text='Enter a')
a_meseage.grid(row=0,column=1)	
b_meseage=Label(root,text='Enter B')
b_meseage.grid(row=2,column=1)	
c_meseage=Label(root,text='Enter C')
c_meseage.grid(row=4,column=1)	



import matplotlib.pyplot as plt
import numpy as np


		
def Quad():
    global a
    global b
    global c
    a=a_input.get()
    b=b_input.get()
    c=c_input.get()
    a=float(a)
    b=float(b)
    c=float(c)
    disc=(b**2)-(4*a*c)
    if disc>0:
        x1 = (-b - math.sqrt(disc)) / (2 * a)
        x2 = (-b + math.sqrt(disc)) / (2 * a)
        roots['text'] = (round(x1,2),'and',round(x2,2))  
        roots_number['text'] = 'Their are two roots'
    elif disc <0:
        roots_number['text'] = 'Imaginary roots'
    elif disc==0 :
        x1 = (-b - math.sqrt(disc)) / (2 * a)
        roots['text'] = x1
        roots_number['text'] = 'Their is a single roots'
    
    discriminent['text']=('discriminent:',disc)
    v=a*b
    if  v==0:
        vertix['text'] =('Vertex is on y-axis')
    elif v>0:
        vertix['text']= ('vertex is left of the orgin')
    elif v<0:
        vertix['text']= ('vertex is right of the orgin')
    if c>0:
        y_intercept['text']= ('Y-intercept is above the orgin')
    elif c<0:
        y_intercept['text']= ('Y-intercept is below the orgin')
    h=(b*-1)/(2*a)
    k=a*(h*h)+b*h+c
    vertix_values['text']= ('Vertix:',round(h,2),round(k,2))
    if a>0:
        shape['text']=('the curve will be shaped like a u')	
    elif a<0:
        shape['text']=('the curve will be shaped like a n')



roots_number=Label(root,text='')
roots_number.grid(row=2,column=2)	
roots=Label(root,text='')
roots.grid(row=3,column=2)	
discriminent=Label(root,text='')
discriminent.grid(row=0,column=2)
vertix=Label(root,text='')
vertix.grid(row=5,column=2)
vertix_values=Label(root,text='')
vertix_values.grid(row=6,column=2)		
shape=Label(root,text='')
shape.grid(row=7,column=2)	
y_intercept=Label(root,text='')
y_intercept.grid(row=8,column=2)	
Start=Button(root,text='Calculate',fg='black',command=Quad)
Start.grid(row=7,column=1)		
root.mainloop()
