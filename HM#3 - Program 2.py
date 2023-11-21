import tkinter
from tkinter import Label, Button, messagebox, simpledialog

#Proceeds to Input
def alohomora():

    #Entering your Current Balance
    Money_Quantity = (simpledialog.askinteger("Money", "How much is your current balance right now?"))
    
    #Asking for how much you will spend on an Apple
    Apple_Quantity = (simpledialog.askinteger("Apples", "How much are you willing to spend on an Apple? It cost Php20 each as of now."))

    #Breakdown of Purchase
    Money_Left = Money_Quantity%Apple_Quantity
    Num_Apple = Money_Quantity//Apple_Quantity
    Total_Cost = Num_Apple*Apple_Quantity

    #Strings for the messagebox
    str_money_quantity = str(Money_Quantity)
    str_apple_quantity = str(Apple_Quantity)
    str_money_left = str(Money_Left)
    str_num_apple = str(Num_Apple)
    str_total_cost = str(Total_Cost)

    #Message of Purchase
    Will_Buy = messagebox.askokcancel(title= "Edwardoorinos", message="Good day! Your current balance as of now is Php" + str_money_quantity + ".  You are willing to buy an Apple for the price of Php" + str_apple_quantity + " and for that you need to spend Php" + str_total_cost + ". Do you wish to proceed?")
    if Will_Buy == True:
        messagebox.showinfo(title= "Purchased", message="Good day! You bought an amount of " + str_num_apple + " apple/s for the price of Php" + str_total_cost + ".  Your remaining balance now is Php" + str_money_left + ". Thank you for purchasing!")
    else:
        messagebox.showinfo(title= "Happy to Serve", message="We hope to see you next time on your next purchase.")

    #Name of Customer
    Name_Input = simpledialog.askstring("Name", "May we know who our customer is?")
    while all((valid.isalpha() or valid.isspace()) for valid in Name_Input) == False:
        messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
        Name_Input = simpledialog.askstring("Name", "May we know who our customer is?")
    while len(Name_Input) == 0:
        messagebox.showwarning("Error", "Please state your name")
        Name_Input = simpledialog.askstring("Name", "May we know who our customer is?")
        while all((valid.isalpha() or valid.isspace()) for valid in Name_Input) == False:
            messagebox.showerror(title="Invalid", message="Please use LETTERS & SPACING ONLY! Thank you :D"),
            Name_Input = simpledialog.askstring("Name", "May we know who our customer is?")
    print (Name_Input)

    #Results
    Name_Label.configure(text=str("It is our pleasure serving you " + Name_Input))


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
Introduction_Label = Label(Ed_Label_Frame, text="  Welcome to Edwardoorinos!  ", font="Heltivica, 25")
Introduction_Label.grid(row=0, column=0, columnspan=2, pady=10)
Introduction_Label.configure(bg= "#F6F4F2")

#Let's Start
Start_Label = Label(Ed_Label_Frame, text="Buy Fresh Apples and Oranges", font="Heltivica, 18")
Start_Label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)
Start_Label.configure(bg= "#F6F4F2")

#Labels
Name_Label = Label(Ed_Label_Frame, font="Impact, 18")
Name_Label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
Name_Label.configure(bg= "#F6F4F2")

#Button to Proceed
Proceed_Button = Button(Ed_Frame, text=("Proceed"), command=alohomora, font='Impact, 16', bd=3)
Proceed_Button.grid(row=2, columnspan=2, padx=10, pady=5, sticky="news")
Proceed_Button.configure(bg= "#FFD02C")

#Button to Cancel
Cancel_Button = Button(Ed_Frame, text=("Exit"), command=exit, font='Impact, 16', bd=3)
Cancel_Button.grid(row=3, columnspan=2, padx=10, pady=15, sticky="news")
Cancel_Button.configure(bg= "#EE5C42")

#Can't resize the root
root.resizable(False, False)

#Looping
root.mainloop()