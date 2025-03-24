# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("OVERCOMING CONTAMINATION OCD PAGE")

# Set the geometry of tkinter frame
win.geometry("600x300")

# Create a canvas
canvas = Canvas(win, width=600, height=300)
canvas.pack()

# Function to open another file
def open_other_file():
    subprocess.Popen(["python", "overcome_symmetry_and_ordering_ocd_page_8.py"])  # Change "other_script.py" to your file
    
# Create a Frame for the button
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Frame
btn = tk.Button(frame, text="OVERCOME SYMMETRY AND ORDERING OCD", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

# Load an image in the script
img = Image.open("contamination_ocd.jpg")

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
canvas.create_text(500, 80, text="OVERCOME THE CONTAMINATION OCD", fill="cyan2", font=('Times 20 bold italic'))
canvas.create_text(500, 110, text="i) MINDFULNESS AND RELAXATION EXERCISES:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 140, text="Practicing mindfulness helps you stay present and manage anxiety by observing", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 150, text="thoughts without judgment. Deep breathing exercises can calm your nervous system", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 160, text="reducing stress and promoting relaxation.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 190, text="ii) DEVELOPING A STRUCTURED ROUTINE:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 220, text="Establishing a daily routine provides stability and reduces uncertainty, which may", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 230, text="trigger OCD symptoms. A predictable schedule with time for work, relaxation, and", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 240, text="hobbies can help manage stress effectively.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 270, text="iii) ADDRESSING SETBACKS AND RELAPSES:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 300, text="Setbacks are a normal part of recovery and do not mean failure. Learning from", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 310, text="these experiences and continuing to use coping strategies can strengthen resilience", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 320, text="and improve OCD management.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 350, text="iv) AVOIDING COMPULSIVE BEHAVIORS:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 380, text="Resisting compulsions is challenging but essential for breaking the cycle of", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 390, text="obsessions. Exposure and Response Prevention (ERP) can help retrain your brain to", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 400, text="reduce the power of intrusive thoughts over time.", fill="white", font=('Times 10 italic'))
# Start the Tkinter event loop
win.mainloop()



