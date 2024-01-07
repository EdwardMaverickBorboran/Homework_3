# Homework 3
# Program 1

# Create a program that will ask
# How many apples and oranges the user wants to buy.
# Display the total amount the user needs to pay
# An Apple cost 20 pesos each
# An Orange cost 25 pesos each
# Display the output

# Deadline: BEFORE NOV. 25, 2023!!!

import tkinter
from tkinter import Label, Button, messagebox, simpledialog

# Proceeds to Buying Apples and Oranges along with indicating your name as the buyer
def open():

    # Apple
    apple_quantity = (simpledialog.askinteger("Apples", "What is your desired amount of Apples? It cost Php 20 each"))
    apple_price = apple_quantity*20
    str_apple_price = str(apple_price)
    messagebox.showinfo(title= "Purchased", message="The total cost of the Apples you purchased is Php " + str_apple_price)

    # Orange
    orange_quantity = (simpledialog.askinteger("Apples", "What is your desired amount of Oranges? It cost Php 25 each"))
    orange_price = orange_quantity*25
    str_orange_price = str(orange_price)
    messagebox.showinfo(title= "Purchased", message="The total cost of the Oranges you purchased is Php " + str_orange_price)

    # Total Cost
    total_cost = apple_price + orange_price
    str_total_cost = str(total_cost)
    messagebox.showinfo(title= "Total Purchase", message="The total cost of your Purchase is Php " + str_total_cost)

    # Name of Buyer
    name_input = simpledialog.askstring("Name", "May we know who is our buyer is?")
    while all((valid.isalpha() or valid.isspace()) for valid in name_input) == False:
        messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
        name_input = simpledialog.askstring("Name", "May we know who is our buyer is?")
    while len(name_input) == 0:
        messagebox.showwarning("Error", "Please state your name")
        name_input = simpledialog.askstring("Name", "May we know who is our buyer is?")
        while all((valid.isalpha() or valid.isspace()) for valid in name_input) == False:
            messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
            name_input = simpledialog.askstring("Name", "May we know who is our buyer is?")
    print (name_input)

    # Results
    name_label.configure(text=str("It is our pleasure to serve you " + name_input))

    messagebox.showinfo("Congratulations!", "Purchased Successful")


# Creation of Edwardoorinos Tab
root = tkinter.Tk()
root.title("EdwardoorinOss")
root.configure(bg= "#31422E")

# Creation of Edwardoorinos Frame
ed_frame = tkinter.Frame(root)
ed_frame.pack(padx=20, pady=20)
ed_frame.configure(bg= "#587E5B")

# Edwardoorinos Frame Interface
label_frame = tkinter.LabelFrame(ed_frame, bd=5)
label_frame.grid(row=0, column=0, padx=20, pady=15)
label_frame.configure(bg= "#F6F4F2")

# Introduction
introduction_label = Label(label_frame, text="  Welcome to Edwardoorinos!  ", font="Impact, 25")
introduction_label.grid(row=0, column=0, columnspan=2, pady=10)
introduction_label.configure(bg= "#F6F4F2")

# Let's Start
start_label = Label(label_frame, text="Buy Fresh Apples and Oranges", font="Impact, 18")
start_label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
start_label.configure(bg= "#F6F4F2")

# Labels
name_label = Label(label_frame, font="Impact, 18")
name_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
name_label.configure(bg= "#F6F4F2")

# Button for Submission
submit_button = Button(ed_frame, text=("Proceed"), command=open, font='Impact, 16', bd=3)
submit_button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="news")
submit_button.configure(bg= "#FFD02C")

# Button to Cancel
cancel_button = Button(ed_frame, text=("Exit"), command=exit, font='Impact, 16', bd=3)
cancel_button.grid(row=3, columnspan=2, padx=10, pady=15, sticky="news")
cancel_button.configure(bg= "#EE5C42")

# Can't resize the root
root.resizable(False, False)

# Looping
root.mainloop()