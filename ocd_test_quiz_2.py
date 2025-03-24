import tkinter as tk
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

class OCDQuiz:
    def display_image(self):
        try:
            image_path = "C:/Users/sheri/OneDrive/Desktop/Creative_Fest_Project/ocd_login.jpg"
            img = Image.open(image_path)
            img = img.resize((1000, 250), Image.Resampling.LANCZOS)  # Resize image
            photo = ImageTk.PhotoImage(img)

            canvas = tk.Canvas(self.root, width=1000, height=250)
            canvas.pack()
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            canvas.image = photo  # Keep reference
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load image: {e}")
            
    def __init__(self, root):
        self.root = root
        self.root.title("OCD Quiz Test")
        
        self.questions = [
            "1. Do you worry about germs, getting sick, or dying?",
            "2. Do you have extreme fears about bad things happening or doing something wrong?",
            "3. Do you feel that things have to be just right?",
            "4. Do you have disturbing and unwanted thoughts or images about hurting others, but don't want to hurt anyone?",
            "5. Do you engage in excessive checking (example: re-checking that the door is locked, that the oven is off)?",
            "6. Are you bothered by thoughts that you find embarrassing or gross?",
            "7. Do you worry a lot about doing a wrong thing?",
            "8. Do you have disturbing and unwanted thoughts or images of sexual nature?",
            "9. Do you engage in excessive washing and/or cleaning?",
            "10. Do you repeat actions until they are just right or starting things over again? (example: making sure phone alarm is on, keep re-writing a paper)?",
            "11. Do you order or arrange things or items?",
            "12. Do you need excessive reassurance (example: always asking, Are you sure I am going to be okay?)?",
            "13. Do you spend more than 3 hours total a day struggling with obsessions or compulsions?"
        ]
        
        self.responses = []
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.create_quiz()
        
        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_score, bg="blue", fg="white")
        self.submit_button.pack(pady=10)

        # Display image
        self.display_image()

    def create_quiz(self):
        for i, question in enumerate(self.questions):
            label = tk.Label(self.frame, text=question, anchor="w")
            label.grid(row=i, column=0, sticky="w", padx=10, pady=5)

            var = tk.StringVar(value="Never")
            self.responses.append(var)

            tk.Radiobutton(self.frame, text="Never", variable=var, value="Never").grid(row=i, column=1)
            tk.Radiobutton(self.frame, text="Sometimes", variable=var, value="Sometimes").grid(row=i, column=2)
            tk.Radiobutton(self.frame, text="Always", variable=var, value="Always").grid(row=i, column=3)

    def calculate_score(self):
        total_score = 0
        for response in self.responses:
            if response.get() == "Always":
                total_score += 10
            elif response.get() == "Sometimes":
                total_score += 5

        if 0 <= total_score <= 43:
            result = "Low OCD"
        elif 44 <= total_score <= 86:
            result = "Moderate OCD"
        else:
            result = "High OCD"

        messagebox.showinfo("OCD Quiz Result", f"Your total score is: {total_score}\nOCD Level: {result}")

# OCD TYPES BUTTON CODE
def open_other_file():
    subprocess.Popen(["python", "ocd_types_page_3.py"])  # Change "other_script.py" to your file

if __name__ == "__main__":
    win = tk.Tk()
    app = OCDQuiz(win)
    
    # OCD Types Button
    btn = tk.Button(win, text="OCD TYPES, CHECKING OCD", command=open_other_file, bg="blue4", fg="misty rose")
    btn.pack(pady=10)
    
    win.mainloop()






