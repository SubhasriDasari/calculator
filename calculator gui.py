# -*- coding: utf-8 -*-
"""
Created on Sun May 18 12:13:26 2025

@author: subhasri
"""

import tkinter as tk
from tkinter import messagebox

def add():
    try:
        result.set(float(entry1.get()) + float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def subtract():
    try:
        result.set(float(entry1.get()) - float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def multiply():
    try:
        result.set(float(entry1.get()) * float(entry2.get()))
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

def divide():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Math Error", "Cannot divide by zero.")
        else:
            result.set(float(entry1.get()) / num2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
        
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.resizable(False, False)


tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()


tk.Button(root, text="Add", width=15, command=add).pack(pady=5)
tk.Button(root, text="Subtract", width=15, command=subtract).pack(pady=5)
tk.Button(root, text="Multiply", width=15, command=multiply).pack(pady=5)
tk.Button(root, text="Divide", width=15, command=divide).pack(pady=5)


result = tk.StringVar()
tk.Label(root, text="Result:").pack(pady=10)
tk.Label(root, textvariable=result, font=('Arial', 14, 'bold')).pack()


root.mainloop()
