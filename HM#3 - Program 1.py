import tkinter
import tkinter.font
from tkinter import Label, Button, messagebox, simpledialog

#Proceeds to Buying Apples and Oranges along with indicating your name as the buyer
def open():

    #Apple
    Apple_Quantity = (simpledialog.askinteger("Apples", "What is your desired amount of Apples? It cost Php 20 each"))
    Apple_Price = Apple_Quantity*20
    str_Apple_Price = str(Apple_Price)
    messagebox.showinfo(title= "Purchased", message="The total cost of the Apples you purchased is Php " + str_Apple_Price)

    #Orange
    Orange_Quantity = (simpledialog.askinteger("Apples", "What is your desired amount of Oranges? It cost Php 25 each"))
    Orange_Price = Orange_Quantity*25
    str_Orange_Price = str(Orange_Price)
    messagebox.showinfo(title= "Purchased", message="The total cost of the Oranges you purchased is Php " + str_Orange_Price)

    #Name of Buyer
    Name_Input = simpledialog.askstring("Name", "May we know who is our buyer is?")
    while all((valid.isalpha() or valid.isspace()) for valid in Name_Input) == False:
        messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
        Name_Input = simpledialog.askstring("Name", "May we know who is our buyer is?")
    while len(Name_Input) == 0:
        messagebox.showwarning("Error", "Please state your name")
        Name_Input = simpledialog.askstring("Name", "May we know who is our buyer is?")
        while all((valid.isalpha() or valid.isspace()) for valid in Name_Input) == False:
            messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
            Name_Input = simpledialog.askstring("Name", "May we know who is our buyer is?")
    print (Name_Input)
        

    Total_Cost = Apple_Price + Orange_Price
    str_Total_Cost = str(Total_Cost)
    messagebox.showinfo(title= "Receipt of Purchase", message="Here is your receipt, the total cost of the your whole purchased is Php " + str_Total_Cost  + " Thank you for shopping! Come again :D")

    #Results
    Name_Label.configure(text=str("It is our pleasure to serve you " + Name_Input))

    messagebox.showinfo("Congratulations!", "Purchased Successful")



#Creation of Edwardoorinos Tab
root = tkinter.Tk()
root.title("Edwardoorinos")
root.configure(bg= "#31422E")

#Creation of Edwardoorinos Frame
Ed_Frame = tkinter.Frame(root)
Ed_Frame.pack(padx=20, pady=20)
Ed_Frame.configure(bg= "#587E5B")

#Edwardoorinos Frame Interface
Ed_Label_Frame = tkinter.LabelFrame(Ed_Frame, bd=5)
Ed_Label_Frame.grid(row=0, column=0, padx=20, pady=15)
Ed_Label_Frame.configure(bg= "#F6F4F2")

#Introduction
Introduction_Label = Label(Ed_Label_Frame, text="  Welcome to Edwardoorinos!  ", font="Impact, 25")
Introduction_Label.grid(row=0, column=0, columnspan=2, pady=10)
Introduction_Label.configure(bg= "#F6F4F2")

#Let's Start
Start_Label = Label(Ed_Label_Frame, text="Buy Fresh Apples and Oranges", font="Impact, 18")
Start_Label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
Start_Label.configure(bg= "#F6F4F2")

#Labels
Name_Label = Label(Ed_Label_Frame, font="Impact, 18")
Name_Label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
Name_Label.configure(bg= "#F6F4F2")

#Button for Submission
Submit_Button = Button(Ed_Frame, text=("Proceed"), command=open, font='Impact, 16', bd=3)
Submit_Button.grid(row=2, columnspan=2, padx=10, pady=15, sticky="news")
Submit_Button.configure(bg= "#FFD02C")

#Can't resize the root
root.resizable(False, False)

#Looping
root.mainloop()