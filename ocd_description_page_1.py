#OCD Description PAGE

#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk
import subprocess


#Create an instance of tkinter frame
win = Tk()
win.title("OCD DESCRIPTION PAGE")

#Set the geometry of tkinter frame
win.geometry("500x250")

#Create a canvas
canvas= Canvas(win, width= 500, height= 250)
canvas.pack()

import tkinter as tk
import subprocess

def open_other_file():
    subprocess.Popen(["python", "ocd_test_quiz_2.py"])  # Change "other_script.py" to your file

# Create a frame widget
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Text widget
btn = tk.Button(frame, text="OCD TEST QUIZ", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

#Load an image in the script
img= (Image.open("ocd_login1.jpg"))

#Resize the Image using resize method
resized_image= img.resize((500,250))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)
#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="skyblue")

#Add a text in Canvas
canvas.create_text(500, 50, text="OBSESSIVE COMPULSIVE DISORDER (OCD)", fill="blue4", font=('Times 30 bold italic'))
canvas.create_text(500, 80, text="Obsessive-compulsive disorder (OCD) is a mental health condition that causes unwanted thoughts and repetitive behaviors.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 95, text="People with OCD may experience significant distress or impairment in their daily lives.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 115, text="SYMPTOMS OF OCD",fill="brown4", font=('Times 15 bold italic'))
canvas.create_text(500, 135, text="Obsessions: Unwanted thoughts, images, or impulses that are persistent and intrusive.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 150, text="Compulsions: Repetitive behaviors that are excessive, time-consuming, and distressing.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 170, text="COMMON EXAMPLES OF OBSESSIONS",fill="magenta4", font=('Times 15 bold italic'))
canvas.create_text(500, 190, text="1. Fear of contamination from germs, dirt, or poisons.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 205, text="2. Fear of harming someone or something.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 220, text="3. Intrusive thoughts about violence, accidents, or sex.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 235, text="4. Fear of being burgled.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 250, text="5. Obsessions related to perfectionism.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 270, text="COMMON EXAMPLES OF COMPULSIONS",fill="red4", font=('Times 15 bold italic'))
canvas.create_text(500, 290, text="1. Repeated hand-washing.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 305, text="2. Checking and rechecking locks, doors, or the stove.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 320, text="3. Following rigid rules of order.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 335, text="4. Counting in certain patterns.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 350, text="5. Silently repeating a prayer or word.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 365, text="6. Trying to replace a bad thought with a good thought.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 385, text="IMPACT",fill="dark green", font=('Times 15 bold italic'))
canvas.create_text(500, 405, text="OCD can cause significant distress or interfere with daily life. Symptoms usually begin over time and tend to vary in how serious they are throughout life.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 425, text="TREATMENT",fill="blue", font=('Times 15 bold italic'))
canvas.create_text(500, 440, text="Treatment is available to help people manage their symptoms and improve their quality of life.",fill="black", font=('Times 12 italic'))
canvas.create_text(500, 455, text="If you keep getting these thoughts and they have an effect on your daily life, speak to your doctor or health visitor.",fill="black", font=('Times 12 italic'))
canvas.pack()
win.mainloop()

