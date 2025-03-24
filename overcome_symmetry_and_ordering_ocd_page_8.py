# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("OVERCOMING SYMMETRY AND ORDERING OCD PAGE")

# Set the geometry of tkinter frame
win.geometry("600x300")

# Create a canvas
canvas = Canvas(win, width=600, height=300)
canvas.pack()

# Function to open another file
def open_other_file():
    subprocess.Popen(["python", "overcome_ruminations_and_intrusive_thoughts_ocd_9.py"])  # Change "other_script.py" to your file
    
# Create a Frame for the button
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Frame
btn = tk.Button(frame, text="OVERCOME RUMINATIONS AND INTRUSIVE THOUGHTS OCD", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

# Load an image in the script
img = Image.open("symmetry_and_ordering_ocd.jpg")

# Resize the Image
resized_image = img.resize((600, 300))
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas
canvas.create_image(10, 10, anchor=NW, image=new_image)

# Create a larger canvas for text content
canvas = Canvas(win, width=1000, height=750, bg="navy")
canvas.pack()

# Add a text in Canvas
canvas.create_text(500, 50, text="FOUR BEST EXERCISES OR PRACTICES TO", fill="cyan2", font=('Times 20 bold italic'))
canvas.create_text(500, 80, text="OVERCOME THE SYMMETRY AND ORDERING OCD", fill="cyan2", font=('Times 20 bold italic'))
canvas.create_text(500, 110, text="i) GRADUAL EXPOSURE (ERP):", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 140, text="Exposure and Response Prevention (ERP) involves gradually confronting anxiety-", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 150, text="triggering situations without engaging in compulsions. Over time,", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 160, text="this reduces distress and helps retrain the brain to tolerate imperfection.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 190, text="ii) MINDFULNESS TECHNIQUES:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 220, text="Practicing mindfulness, such as meditation and deep breathing,", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 230, text="can help regulate emotions and reduce the urge to correct asymmetry.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 240, text="It shifts focus from obsessive thoughts to present-moment awareness.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 270, text="iii) COGNITIVE-BEHAVIORAL THERAPY (CBT):", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 300, text="CBT helps individuals identify and", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 310, text="challenge irrational thoughts related to symmetry and ordering. By restructuring", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 320, text="these thoughts, it reduces anxiety and the need for compulsions.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 350, text="iv) SUPPORT SYSTEMS:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 380, text="Engaging with supportive family, friends, or therapy groups", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 390, text="can provide encouragement and accountability. Having others to help navigate", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 400, text="triggers can make the recovery process more manageable.", fill="white", font=('Times 10 italic'))
# Start the Tkinter event loop
win.mainloop()



