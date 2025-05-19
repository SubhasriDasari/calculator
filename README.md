# calculator
This project is a Simple Calculator built using Python's Tkinter GUI library. It provides a graphical interface for users to perform basic arithmetic operations — Addition, Subtraction, Multiplication, and Division — on two input numbers.
Key Features:
GUI-based user interface using Tkinter.

Four arithmetic operations: Add, Subtract, Multiply, Divide.

Handles invalid input and division by zero errors gracefully with error messages.

Displays the result dynamically in a label.

Code Explanation:
1. Imports:
import tkinter as tk
from tkinter import messagebox
tkinter: Used to create the GUI components.

messagebox: Used to show popup alerts for errors (e.g., invalid inputs).

2. Function Definitions:
Each operation (add, subtract, multiply, divide) fetches numbers from the input fields and performs calculations. Errors are handled using try-except.

Example:

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
Uses entry1.get() and entry2.get() to retrieve inputs.

Converts them to float.

Displays result using result.set(...).

Shows error pop-up if inputs are not valid numbers.

3. GUI Layout

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
Creates main window with fixed size and title.

Inputs:

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
Two input fields for numbers.

Operation Buttons:

tk.Button(root, text="Add", command=add).pack()
Buttons linked to respective functions.

Result Display:

result = tk.StringVar()
tk.Label(root, textvariable=result).pack()
StringVar is used to dynamically update the result label.

Error Handling:
Invalid Input: Shows error if user enters letters or symbols.

Division by Zero: Shows a specific error if the second number is 0.

