# S M Chow Worn

# **********************************************************************
# Calculator with GUI (Graphic User Interface)
# **********************************************************************

from tkinter import * # Import the tkinter library 

def button_press(num): # Defining each button press
    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals(): # This block checks for the button_press(equals)
    global equation_text

    try: # Try is used in try... except blocks. It defines a block of code if it contains any errors.
         # You can define different blocks for different error types, and blocks to execute.

        total = str(eval(equation_text)) # Parses the expression argument and evaluates it as a python expression.

        equation_label.set(total) #

        equation_text = total

    except SyntaxError: # Check for syntax error

        equation_text.set ("Syntax error")

        equation_text = ""

    except ZeroDivisionError: # Check for division zero

        equation_label.set("Arithmetic error")

        equation_text = ""

def clear(): # Clear the equation_label for the next calcualtion
    global equation_text

    equation_label.set("")

    equation_text = ""

# Designing the user interface


window = Tk() # You can use window, root,... or a descriptive variable of your own
window.title("Calculator Program") # Title of the window bar
window.geometry("500x500")
window.configure(bg="lightBlue")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('console, 20'), bg="lightBlue", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press("1"))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press("2"))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press("3"))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press("4"))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press("5"))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press("6"))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press("7"))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press("8"))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press("9"))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press("0"))
button0.grid(row=3, column=1)

# Create operation buttons

plus = Button(frame, bg = "lightGrey", text='+', height=4, width=9, font=35, command=lambda: button_press("+"))
plus.grid(row=0, column=3)

minus = Button(frame, bg = "lightGrey", text='-', height=4, width=9, font=35, command=lambda: button_press("-"))
minus.grid(row=1, column=3)

filler = Button(frame, bg = "lightGrey", text=' ', height=4, width=9, font=35)
filler.grid(row=3, column=0)

filler_2 = Button(frame, bg = "lightGrey", text=' ', height=4, width=9, font=35)
filler_2.grid(row=3, column=2)

filler_3 = Button(frame, bg = "lightGrey", text=' ', height=4, width=9, font=35)
filler_3.grid(row=3, column=3)

# Create equals button

equals = Button(frame, bg = "lightGrey", text='=', height=4, width=9, font=35, command=equals)
equals.grid(row=2, column=3)

# Create clear button

clear = Button(window, bg = "lightGrey", text='Clear', height=8, width=18, font=35, command=clear)

clear.pack()

window.mainloop()