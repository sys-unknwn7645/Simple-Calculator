from tkinter import *
from tkinter import ttk

window = Tk()

# Window size and Frame
window.title("Calculator")
window.geometry('400x150')
parent1 = ttk.Frame(window).grid()

value = ""

# Clear Function
def clear():
    global value
    value = ""
    output.set(value)
    outdis.config(text=value)
    inpt.delete(0, END)
    inpt.focus()


# Feed function shows what is being calculated
def feed(opr):
    global value

    value_eval = eval(value + info.get())
    value = str(value_eval) + opr
    outdis.config(text=value)
    info.set("")


# Function processes numbers entered with buttons
def click(a):
    info_tmp = info.get()
    info.set(info_tmp + a)

# Calculates the final result
def Calculate(*arg):
    try:
        outdis.config(text=value + info.get())
        output.set(eval(value + info.get()))
    except:
        output.set("Error")

# Setup of the operator buttons
ttk.Button(parent1, text="+", command=lambda: feed("+")).grid(row=0, column=0)
ttk.Button(parent1, text="-", command=lambda: feed("-")).grid(row=0, column=1)
ttk.Button(parent1, text="*", command=lambda: feed("*")).grid(row=1, column=0)
ttk.Button(parent1, text="/", command=lambda: feed("/")).grid(row=1, column=1)
ttk.Button(parent1, text="=", command=Calculate).grid(row=1, column=2)

# User input box
info = StringVar()
inpt = ttk.Entry(parent1, width=25, textvariable=info)
inpt.grid(row=0, column=3)

# Displays what is being calcuated. Output of feed function displays here
outdis = ttk.Label(parent1, text="")
outdis.grid(row=1, column=3)
ttk.Label(parent1, text="=").grid(row=2, column=3)

# Final calculation output is displayed here
output = StringVar()
ttk.Label(parent1, textvariable=output).grid(row=3, column=3)

# clearn Button
ttk.Button(parent1, text="Clear", command=clear).grid(row=0, column=2)

# Number buttons
ttk.Button(parent1, text="1", command=lambda: click("1")).grid(row=2, column=0)
ttk.Button(parent1, text="2", command=lambda: click("2")).grid(row=2, column=1)
ttk.Button(parent1, text="3", command=lambda: click("3")).grid(row=2, column=2)
ttk.Button(parent1, text="4", command=lambda: click("4")).grid(row=3, column=0)
ttk.Button(parent1, text="5", command=lambda: click("5")).grid(row=3, column=1)
ttk.Button(parent1, text="6", command=lambda: click("6")).grid(row=3, column=2)
ttk.Button(parent1, text="7", command=lambda: click("7")).grid(row=4, column=0)
ttk.Button(parent1, text="8", command=lambda: click("8")).grid(row=4, column=1)
ttk.Button(parent1, text="9", command=lambda: click("9")).grid(row=4, column=2)
ttk.Button(parent1, text="0", command=lambda: click("0")).grid(row=5, column=1)

# Keeps the user input box in focus
inpt.focus()

# Assigns keywork 'Return' key to Calculate function
window.bind('<Return>', Calculate)

window.mainloop()