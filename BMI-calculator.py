# Chandigarh University - Winning Camp 2022
# Project - BMI Calculator
# Name - Gurleen Kaur
# UID - 21MCA2157
# File Created - 23/06/2022

# This program is a BMI Calculator. The user can calculate their Body Mass Index using this program. 

# The Body Mass Index or BMI is calculated from weight and height of a Person. 
# It is obtained by dividing an individual’s weight in kilograms by their height in meters, 
# then dividing the answer again by their height.

# The GUI takes the weight of the user (in kilograms) and the height (in meters) as input
# Followed by displaying the BMI as the output. 

# Dependencies used in this program 
# Tkinter - Tkinter is the Python interface to the Tk GUI toolkit shipped with Python.
# messagebox - MessageBox Widget is used to display the message boxes in the python applications. 
# This module is used to display a message using provides a number of functions.

# What is Tk? 
# Tk is a graphical user interface toolkit that takes developing desktop applications 
# to a higher level than conventional approaches.
# Tk is the standard GUI not only for dynamic languages, and can produce rich, 
# native applications that run unchanged across Windows, Mac OS X, Linux and more.


#importing Dependencies
from tkinter import *
from tkinter import messagebox

def reset_inputs():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())  
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} Underweight')
    elif (bmi > 18.5) and (bmi < 24.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} Normal')
    elif (bmi > 24.9) and (bmi < 29.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} Overweight')
    elif (bmi > 29.9) and (bmi < 34.9):
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} Obese') 
    elif (bmi > 34.9):
         messagebox.showinfo('BMI Calculator', f'BMI = {bmi} Extremely Obese') 
    else:
        messagebox.showerror('BMI Calculator', 'something went wrong!')


ws = Tk() # creating a tkinter window
ws.title('BMI Calculator - Gurleen Kaur')
ws.geometry('400x300')

var = IntVar() # Holds an integer; default value 0

frame = Frame(
    ws,
    padx=10, # horizontal padding
    pady=10 # vertical padding
)
frame.pack(expand=True) 
#layout manager, the pack() method declares the position of widgets in relation to each other
# Here is the list of possible options −
# expand − When set to true, widget expands to fill any space not otherwise used in widget's parent.
# fill − Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally and vertically).
# side − Determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT.

age_lb = Label(
    frame,
    text="Enter Age"
)

age_lb.grid(row=1, column=1)
#input, used to Enter or display a single line of text. 
age_tf = Entry( frame, )

age_tf.grid(row=1, column=2, pady=5)
gen_lb = Label(  frame, text='Select Gender')

gen_lb.grid(row=2, column=1)

frame2 = Frame( frame )
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=RIGHT)
height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_inputs
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()