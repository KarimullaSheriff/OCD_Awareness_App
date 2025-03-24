# Import the required Libraries
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import subprocess

# Create an instance of tkinter frame
win = Tk()
win.title("THANK YOU PAGE")

# Set the geometry of tkinter frame
win.geometry("850x850")

# Create a canvas
canvas = Canvas(win, width=1000, height=1000)
canvas.pack()

# Load an image in the script
img = Image.open("thank_you.jpg")

# Resize the Image
resized_image = img.resize((850, 850))
new_image = ImageTk.PhotoImage(resized_image)

# Add image to the Canvas
canvas.create_image(10, 10, anchor=NW, image=new_image)

win.mainloop()
