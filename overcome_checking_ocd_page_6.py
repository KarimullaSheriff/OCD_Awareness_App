# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("OVERCOMING CHECKING OCD PAGE")

# Set the geometry of tkinter frame
win.geometry("600x300")

# Create a canvas
canvas = Canvas(win, width=600, height=300)
canvas.pack()

# Function to open another file
def open_other_file():
    subprocess.Popen(["python", "overcome_contamination_ocd_page_7.py"])  # Change "other_script.py" to your file
    
# Create a Frame for the button
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Frame
btn = tk.Button(frame, text="OVERCOME CONTAMINATION OCD", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

# Load an image in the script
img = Image.open("overcome_checking_ocd.jpg")

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
canvas.create_text(500, 80, text="OVERCOME THE CHECKING OCD", fill="cyan2", font=('Times 20 bold italic'))
canvas.create_text(500, 110, text="i) MINDFULNESS MEDITATION:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 140, text="This practice helps individuals become aware of their thoughts and feelings in the", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 150, text="moment, allowing them to observe intrusive thoughts without reacting to them and", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 160, text="reducing the urge to check.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 190, text="ii) DEEP BREATHING EXERCISES:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 220, text="A simple relaxation technique that can quickly calm anxiety and provide a sense of", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 230, text="control when faced with the urge to check.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 260, text="iii) EXPOSURE AND RESPONSE PREVENTION (ERP):", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 290, text="A therapy approach where individuals are gradually exposed to situations that trigger", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 300, text="their anxieties, while actively resisting the urge to perform their compulsive checking", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 310, text="behaviors.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 340, text="iv) COGNITIVE RESTRUCTURING:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 370, text="This involves identifying and challenging negative thoughts associated with checking", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 380, text="behaviors, replacing them with more realistic and helpful thoughts.", fill="white", font=('Times 10 italic'))
# Start the Tkinter event loop
win.mainloop()



