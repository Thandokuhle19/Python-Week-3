from customtkinter import *
import csv
import customtkinter
import tkinter as tk
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def view_groups():
    print("View Groups")

def add_group():
    print("Add Group")

root = tk.Tk()
root.title("Menu GUI")
root.geometry("400x500")

# Configure styles
root.configure(background="#D8BFD8")  # Mix of grey and purple background

# Welcome message label
welcome_label = tk.Label(root, text="Welcome to the Group Manager!", font=("Arial", 16, "bold"), fg="black")  # Bold black font
welcome_label.pack(pady=20)

# Button to view groups
view_button = tk.Button(root, text="View Groups", command=view_groups, font=("Arial", 12), fg="black")  # Purple button with black font
view_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

# Button to add groups
add_button = tk.Button(root, text="Add Group", command=add_group, font=("Arial", 12), fg="black")  # Purple button with black font
add_button.pack(pady=10, padx=20, ipadx=10, ipady=5, fill=tk.X)

root.mainloop()