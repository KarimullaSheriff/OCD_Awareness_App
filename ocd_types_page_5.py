# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("RUMINATIONS AND INTRUSIVE THOUGHTS OCD PAGE")

# Set the geometry of tkinter frame
win.geometry("800x400")

# Create a canvas
canvas = Canvas(win, width=800, height=400)
canvas.pack()

# Function to open another file
def open_other_file():
    subprocess.Popen(["python", "overcome_checking_ocd_page_6.py"])  # Change "other_script.py" to your file
    
# Create a Frame for the button
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Frame
btn = tk.Button(frame, text="OVERCOME CHECKING OCD", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

# Load an image in the script
img = Image.open("ruminations_and_intrusive_thoughts_ocd.jpg")

# Resize the Image
resized_image = img.resize((800, 400))
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas
canvas.create_image(10, 10, anchor=NW, image=new_image)

# Create a larger canvas for text content
canvas = Canvas(win, width=1000, height=750, bg="navy")
canvas.pack()

# Add a text in Canvas
canvas.create_text(500, 50, text="4. RUMINATIONS AND INTRUSIVE THOUGHTS OCD", fill="cyan2", font=('Times 30 bold italic'))
canvas.create_text(500, 80, text="Ruminations and Intrusive Thoughts OCD involves persistent, distressing thoughts—", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 95, text="often violent, sexual, or blasphemous—that conflict with personal values, leading to", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 110, text="mental rituals like silent prayers or counting to reduce anxiety.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 140, text="FOUR MAIN SYMPTOMS OF", fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 185, text="RUMINATIONS AND INTRUSIVE THOUGHTS OCD", fill="misty rose", font=('Times 30 bold italic'))
canvas.create_text(500, 215, text="i) Distressing thoughts: Repetitive thoughts that cause distress, such as thoughts of harming oneself or others.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 230, text="ii) Obsessions: Obsessive thoughts about death, mortality, or perfection.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 245, text="iii) Worrying: Excessive worrying about the future or dwelling on past mistakes.", fill="white", font=('Times 12 italic'))
canvas.create_text(500, 260, text="iv) Fear: Fear of contamination, injury, or other negative events.", fill="white", font=('Times 12 italic'))
# Start the Tkinter event loop
win.mainloop()



