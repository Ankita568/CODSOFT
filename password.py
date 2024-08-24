import random
from tkinter import messagebox
from tkinter import *

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror(message="Please enter valid inputs for length and repetition")
        return
    
    if length <= 0:
        messagebox.showerror(message="Password length must be a positive integer")
        return
    
    if repeat == 1:
        if length > len(character_string):
            messagebox.showerror(message="Length exceeds the unique character set size for no repetition")
            return
        password = random.sample(character_string, length)
    else:
        password = random.choices(character_string, k=length)
    
    password = ''.join(password)
    password_v.set("Created password: " + password)

character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

password_gen = Tk()
password_gen.geometry("400x250")
password_gen.title("Password Generator")
password_gen.config(bg="#e0f7fa")

# Title of the app
title_label = Label(password_gen, text="Password Generator", font=('Helvetica', 18, 'bold'), bg="#e0f7fa")
title_label.pack(pady=10)

# Read length
length_label = Label(password_gen, text="Enter length of password: ", font=('Arial', 12), bg="#e0f7fa")
length_label.place(x=20, y=50)
length_entry = Entry(password_gen, width=5, font=('Arial', 12))
length_entry.place(x=240, y=50)

# Read repetition
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ", font=('Arial', 12), bg="#e0f7fa")
repeat_label.place(x=20, y=90)
repeat_entry = Entry(password_gen, width=5, font=('Arial', 12))
repeat_entry.place(x=310, y=90)

# Generate password button
password_button = Button(password_gen, text="Generate Password", command=generate_password, font=('Arial', 12), bg="#4df0e1", fg="white")
password_button.place(x=130, y=130)

# Display generated password
password_v = StringVar()
password_label = Label(password_gen, textvariable=password_v, font=('Arial', 12), bg="#e0f7fa", wraplength=350)
password_label.place(x=10, y=180)

# Exit and close the app
password_gen.mainloop()
