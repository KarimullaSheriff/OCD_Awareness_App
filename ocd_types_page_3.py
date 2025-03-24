# Types Of OCD

#Import the required Libraries
from tkinter import *
from PIL import Image,ImageTk

#Create an instance of tkinter frame
win = Tk()
win.title("OCD TYPES AND CHECKING OCD PAGE")
#Set the geometry of tkinter frame
win.geometry("600x300")

#Create a canvas
canvas= Canvas(win, width= 600, height= 300)
canvas.pack()

#CONTAMINATION OCD BUTTON
import tkinter as tk
import subprocess

def open_other_file():
    subprocess.Popen(["python", "ocd_types_page_4.py"])  # Change "other_script.py" to your file

# Create a frame widget
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Text widget
btn = tk.Button(win, text="CONTAMINATION, SYMMETRY AND ORDERING OCD", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

#Load an image in the script
img= (Image.open("ocd_types.jpg"))

#Resize the Image using resize method
resized_image= img.resize((600,300))
new_image= ImageTk.PhotoImage(resized_image)

#Add image to the Canvas Items
canvas.create_image(10,10, anchor=NW, image=new_image)
#Create a canvas object
canvas= Canvas(win, width= 1000, height= 750, bg="navy")

#Add a text in Canvas
canvas.create_text(500, 50, text="TYPES OF OBSESSIVE COMPULSIVE DISORDER", fill="cyan2", font=('Times 30 bold italic'))
canvas.create_text(500, 80, text="1. Checking OCD.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 95, text="2. Contamination OCD.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 110, text="3. Symmetry and Ordering OCD.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 125, text="4. Ruminations and Intrusive Thoughts OCD.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 155, text="1. CHECKING OCD",fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 185, text="Checking OCD involves persistent doubts and compulsive checking behaviors, driven by fear of harm,",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 205, text="leading to anxiety and excessive reassurance-seeking.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 235, text="FOUR MAIN SYMPTOMS OF CHECKING OCD",fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 265, text="i) Persistent, unwanted thoughts about causing harm or danger, such as fearing that a door is unlocked,",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 280, text="such as checking locks multiple times, verifying appliances are off, or asking for reassurance from others.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 295, text="ii) Repetitive actions performed to reduce the anxiety caused by the intrusive thoughts,",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 310, text="such as checking locks multiple times, verifying appliances are off, or asking for reassurance from others.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 325, text="iii) Intense fear that something terrible will happen if the checking rituals are not",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 340, text="performed, such as a fire, injury, or a mistake being exposed.",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 355, text="iv) Difficulty trusting one's own memory or actions, leading to a constant need for",fill="white", font=('Times 12 italic'))
canvas.create_text(500, 370, text="verification and checking.",fill="white", font=('Times 12 italic'))
canvas.pack()
win.mainloop()

