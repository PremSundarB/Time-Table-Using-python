import tkinter as tk
from tkinter import colorchooser
import datetime

def save_timetable():
    pass
    # Retrieve timetable data from GUI fields
    # Implement validation and save logic here
    # Send the message to your email or mobile number

def emptyspace():
    empty_line = tk.Label(window, text="",bg="grey25")
    empty_line.pack()

# Create the main window
window = tk.Tk()
window.title("Timetable Creator")

# Set the size of the window
window.geometry("600x600")  


# Create and arrange GUI elements

label = tk.Label(window, text="Time Table Planner",fg='white',font=("Arial", 18, "bold"),bg='grey23')
label.pack()

emptyspace()
# Available options for AM and PM
time_options = ["AM", "PM"]

# Variable to store the selected time
time_var = tk.StringVar()
time_var.set(time_options[0])  # Set the initial value

option_menu = tk.OptionMenu(window, time_var, *time_options)
option_menu.pack()

emptyspace()

button = tk.Button(window, text="Save", command=save_timetable)
button.pack()

# Get the color based on the current time

window.configure(background="grey25")

# Start the main event loop
window.mainloop()
