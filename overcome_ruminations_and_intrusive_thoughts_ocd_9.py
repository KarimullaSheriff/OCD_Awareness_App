# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("OVERCOMING RUMINATIONS AND INTRUSIVE THOUGHTS OCD PAGE")

# Set the geometry of tkinter frame
win.geometry("600x300")

# Create a canvas
canvas = Canvas(win, width=600, height=300)
canvas.pack()

# Function to open another file
def open_other_file():
    subprocess.Popen(["python", "thank_you_page_10.py"])  # Change "other_script.py" to your file
    
# Create a Frame for the button
frame = Frame(win, bg="blue4")
frame.pack(pady=0.5)

# Create a Button inside the Frame
btn = tk.Button(frame, text="END", command=open_other_file, bg="blue4", fg="misty rose")
btn.pack()

# Load an image in the script
img = Image.open("ruminations_and_intrusive_thoughts_ocd2.jpg")

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
canvas.create_text(500, 80, text="OVERCOME THE RUMINATIONS AND INTRUSIVE THOUGHTS OCD", fill="cyan2", font=('Times 20 bold italic'))
canvas.create_text(500, 110, text="i) PRACTICE MINDFULNESS MEDITATION:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 140, text="Mindfulness meditation helps you observe intrusive thoughts without judgment,", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 150, text="reducing their emotional impact. By focusing on your breath or bodily sensations,", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 160, text="you learn to let thoughts pass without engaging with them.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 190, text="ii) TRY VISUALIZATION TECHNIQUES:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 220, text="Visualization involves imagining a peaceful scene or mentally", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 230, text="placing intrusive thoughts inside a box and setting them aside. This technique helps", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 240, text="create psychological distance from distressing thoughts, reducing their power over you.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 270, text="iii) DISTRACT YOURSELF WITH AN ENGAGING TASK:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 300, text="Engaging in activities like reading, puzzles,", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 310, text="or exercise shifts your focus away from intrusive thoughts. Keeping your mind occupied", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 320, text="helps break the cycle of rumination and prevents obsessive thinking.", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 350, text="iv) TRY GROUNDING TECHNIQUES, SUCH AS HOLDING A SMALL OBJECT:", fill="misty rose", font=('Times 15 bold italic'))
canvas.create_text(500, 380, text=" Holding and focusing on a textured object, such as a stone or stress ball,", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 390, text="anchors you to the present moment. This sensory experience redirects attention", fill="white", font=('Times 10 italic'))
canvas.create_text(500, 400, text="from intrusive thoughts to the physical world, reducing anxiety.", fill="white", font=('Times 10 italic'))
# Start the Tkinter event loop
win.mainloop()



