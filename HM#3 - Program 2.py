# Homework 3
# Program 2

# Create a program which you will enter
# The amount of money the user has.
# It will also ask for the price of an apple.
# Display the maximum number of apples that the user can buy.
# Display the remaining money that the user will get
# Display the output

# Deadline: BEFORE NOV. 25, 2023!!!

import tkinter
from tkinter import Label, Button, messagebox, simpledialog

# Proceeds to Input
def alohomora():

    # Entering your Current Balance
    money_quantity = (simpledialog.askinteger("Money", "How much is your current balance right now?", minvalue=0))
    
    # Asking for how much you will spend on an Apple
    apple_quantity = (simpledialog.askinteger("Apples", "How much are you willing to spend on an Apple? It cost Php20 each as of now.", minvalue=10))

    # Breakdown of Purchase
    money_left = money_quantity%apple_quantity
    num_apple = money_quantity//apple_quantity
    total_cost = num_apple*apple_quantity

    # Strings for the messagebox
    str_money_quantity = str(money_quantity)
    str_apple_quantity = str(apple_quantity)
    str_money_left = str(money_left)
    str_num_apple = str(num_apple)
    str_total_cost = str(total_cost)

    # Message of Purchase
    will_buy_product = messagebox.askokcancel(title= "Edwardoorinos", message="Good day! Your current balance as of now is Php" + str_money_quantity + ".  You are willing to buy an Apple for the price of Php" + str_apple_quantity + " and for that you need to spend Php" + str_total_cost + ". Do you wish to proceed?")
    if will_buy_product == True:
        messagebox.showinfo(title= "Purchased", message="Good day! You bought an amount of " + str_num_apple + " apple/s for the price of Php" + str_total_cost + ".  Your remaining balance now is Php" + str_money_left + ". Thank you for purchasing!")
    else:
        messagebox.showinfo(title= "Happy to Serve", message="We hope to see you next time on your next purchase.")

    # Name of Customer
    name_input = simpledialog.askstring("Name", "May we know who our customer is?")
    while all((valid.isalpha() or valid.isspace()) for valid in name_input) == False:
        messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
        name_input = simpledialog.askstring("Name", "May we know who our customer is?")
    while len(name_input) == 0:
        messagebox.showwarning("Error", "Please state your name")
        name_input = simpledialog.askstring("Name", "May we know who our customer is?")
        while all((valid.isalpha() or valid.isspace()) for valid in name_input) == False:
            messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
            name_input = simpledialog.askstring("Name", "May we know who our customer is?")
    print (name_input)

    # Results
    name_label.configure(text=str("It is our pleasure serving you " + name_input))

# Creation of Edwardoorinos Tab
root = tkinter.Tk()
root.title("Edwardoorinos")
root.configure(bg= "#31422E")

# Creation of Edwardoorinos Frame
ed_frame = tkinter.Frame(root)
ed_frame.pack(padx=20, pady=20)
ed_frame.configure(bg= "#587E5B")

# Edwardoorinos Frame Interface
ed_label_frame = tkinter.LabelFrame(ed_frame, bd=5)
ed_label_frame.grid(row=0, column=0, padx=20, pady=15)
ed_label_frame.configure(bg= "#F6F4F2")

# Introduction
introduction_label = Label(ed_label_frame, text="  Welcome to Edwardoorinos!  ", font="Heltivica, 25")
introduction_label.grid(row=0, column=0, columnspan=2, pady=10)
introduction_label.configure(bg= "#F6F4F2")

# Let's Start
start_label = Label(ed_label_frame, text="APPLES! APPLES! APPLES!", font="Heltivica, 18")
start_label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
start_label.configure(bg= "#F6F4F2")

# Labels
name_label = Label(ed_label_frame, font="Impact, 18")
name_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
name_label.configure(bg= "#F6F4F2")

# Button to Proceed
proceed_button = Button(ed_frame, text=("Proceed"), command=alohomora, font='Impact, 16', bd=3)
proceed_button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="news")
proceed_button.configure(bg= "#FFD02C")

#Button to Cancel
cancel_button = Button(ed_frame, text=("Exit"), command=exit, font='Impact, 16', bd=3)
cancel_button.grid(row=3, columnspan=2, padx=10, pady=15, sticky="news")
cancel_button.configure(bg= "#EE5C42")

#Can't resize the root
root.resizable(False, False)

#Looping
root.mainloop()
