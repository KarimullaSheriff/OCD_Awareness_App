# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("CONTAMINATION OCD, SYMMETRY AND ORDERING OCD PAGE")

# Set the geometry of tkinter frame
win.geometry("500x250")

# Create a canvas
canvas = Canvas(win, width=500, height=250)
canvas.pack()

# Function to open another file
def open_other_file():
    subprocess.Popen(["python", "ocd_types_page_5.py"])  # Change "other_script.py" to your file

# Create a Frame for the button
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Frame
btn = tk.Button(frame, text="RUMINATIONS AND INTRUSIVE THOUGHTS OCD", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

# Load an image in the script
img = Image.open("contamination_ocd_symmetry_and_ordering_ocd.jpg")

# Resize the Image
resized_image = img.resize((500, 250))
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas
canvas.create_image(10, 10, anchor=NW, image=new_image)

# Create a larger canvas for text content
canvas = Canvas(win, width=1000, height=750, bg="navy")
canvas.pack()

# Add a text in Canvas
canvas.create_text(500, 50, text="2. CONTAMINATION OCD", fill="cyan2", font=('Times 30 bold italic'))
canvas.create_text(500, 80, text="Contamination OCD involves an intense fear of germs or dirt, leading to excessive cleaning, avoidance behaviors, and rituals that disrupt daily life.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 110, text="FOUR MAIN SYMPTOMS OF CONTAMINATION OCD", fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 140, text="i) Fear of contamination: An intense fear of germs, dirt, chemicals, or other contaminants.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 155, text="ii) Compulsive cleaning: Excessive handwashing, showering, or cleaning.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 170, text="iii) Avoidance: Avoiding public places or physical contact.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 185, text="iv) Distress: Distress in environments perceived as unclean.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 215, text="3. SYMMETRY AND ORDERING OCD", fill="cyan2", font=('Times 30 bold italic'))
canvas.create_text(500, 245, text="Symmetry and Ordering OCD involves a compulsive need for alignment, balance, and order,", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 260, text="causing distress and repetitive behaviors when perfection isn't achieved.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 290, text="FOUR MAIN SYMPTOMS OF", fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 335, text="SYMMETRY AND ORDERING OCD", fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 365, text="i) Compulsions: The need to arrange objects in a specific order or symmetrically.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 380, text="ii) Distress: Feeling distressed when things are not in order or aligned.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 395, text="iii) Rituals: Repeating behaviors or counting rituals to a specific number.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 410, text="iv) Magical thinking: Believing that order prevents negative outcomes.", fill="white", font=('Times 12 italic'))

# Start the Tkinter event loop
win.mainloop()



