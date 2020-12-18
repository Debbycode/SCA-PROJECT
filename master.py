#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:00:50 2020

@author: mac
"""

#Importing Modules
import tkinter as tk
import student_database as sd
from PIL import ImageTk
from PIL import Image

mainWindow = tk.Tk()
mainWindow.title('Student Management System | SCA Cohort3 Mentorship')
mainWindow.configure(bg= 'thistle1')

#(She Code Africa Logo)
filename = 'SCALOGO.PNG'
img = Image.open(filename)
resized_img = img.resize((60, 60))

mainWindow.photoimg = ImageTk.PhotoImage(resized_img)
labelimage = tk.Label(mainWindow, image=mainWindow.photoimg)
labelimage.place(relx=0.5,
                 rely=0.03,
                 anchor='center')

#Specicifying the colours and Fonts for the LABEL1

label_1 = tk.Label(mainWindow, text="\n  SCA UNIVERSITY STUDENT MANAGEMENT PORTAL  \n", bg='thistle1', fg='DeepPink4', font=("Georgia", 30))
label_1.pack(padx=100, pady=50)


#specificying the BUTTONS colours and commands colour
button_1 = tk.Button(mainWindow, text="Add Student", fg = 'DeepPink4', command=lambda: sd.insert(), padx=275, pady=25,
                     activebackground='grey', activeforeground='white')
button_1.pack()

button_2 = tk.Button(mainWindow, text="Update Student Details", fg = 'DeepPink4', command=lambda: sd.update(), padx=240, pady=25,
                     activebackground='grey', activeforeground='white')
button_2.pack()

button_3 = tk.Button(mainWindow, text="View Student Details", fg = 'DeepPink4', command=lambda: sd.display(), padx=248, pady=25,
                     activebackground='grey', activeforeground='white')
button_3.pack()

button_4 = tk.Button(mainWindow, text="Delete Student", fg = 'DeepPink4', command=lambda: sd.delete(), padx=267, pady=25,
                     activebackground='grey', activeforeground='white')
button_4.pack()

button_5 = tk.Button(mainWindow, text="Search Student", fg = 'DeepPink4', command=lambda: sd.search(), padx=267, pady=25,
                     activebackground='grey', activeforeground='white')
button_5.pack()


#Specicifying the colours and Fonts for the LABEL2

label_2 = tk.Label(mainWindow, text="Designed by Deborah Ajah (GITHUB: @DebbyCode). ", font=('arial', 12), bg = 'thistle1', fg='maroon4')
label_2.place(relx=0.0,
              rely=1.0,
              anchor='sw')


mainWindow.mainloop()
