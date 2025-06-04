import tkinter as tk

# Functions for each operation
def add():
    result = float(entry1.get()) + float(entry2.get())
    result_label.config(text="Result: " + str(result))

def subtract():
    result = float(entry1.get()) - float(entry2.get())
    result_label.config(text="Result: " + str(result))

def multiply():
    result = float(entry1.get()) * float(entry2.get())
    result_label.config(text="Result: " + str(result))

def divide():
    if float(entry2.get()) != 0:
        result = float(entry1.get()) / float(entry2.get())
        result_label.config(text="Result: " + str(result))
    else:
        result_label.config(text="Error: Cannot divide by 0")

# 
window = tk.Tk()
window.title("Simple Calculator")

# Input fields
tk.Label(window, text="Enter number A").grid(row=0, column=0)
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

tk.Label(window, text="Enter number B").grid(row=1, column=0)
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

# Buttons
tk.Button(window, text="Add", command=add).grid(row=2, column=0)
tk.Button(window, text="Subtract", command=subtract).grid(row=2, column=1)
tk.Button(window, text="Multiply", command=multiply).grid(row=3, column=0)
tk.Button(window, text="Divide", command=divide).grid(row=3, column=1)

# Result Label
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

# Run the application
window.mainloop()
