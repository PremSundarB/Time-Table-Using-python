import tkinter as tk

def save_timetable():
    pass
    # Retrieve timetable data from GUI fields
    # Implement validation and save logic here
    # Send the message to your email or mobile number

def emptyspace():
    empty_line = tk.Label(window, text="", bg="grey25")
    empty_line.grid(pady=40)

# Create the main window
window = tk.Tk()
window.title("Timetable Creator")

# Set the size of the window
window.geometry("600x600")

# Configure the grid size
window.grid_columnconfigure(0, minsize=100)  # Set the minimum width for column 0
window.grid_columnconfigure(1, minsize=200)  # Set the minimum width for column 1
window.grid_columnconfigure(2, minsize=300)  # Set the minimum width for column 1

# Create and arrange GUI elements

# Title
label = tk.Label(window, text="Time Table Planner", fg='white', font=("Arial", 18, "bold"), bg='grey23')
label.grid(pady=10)

# DropDown Menu for time entry
hour_options = [str(i) for i in range(1, 13)]
minute_options = ['00', '15', '30', '45']
period_options = ["AM", "PM"]

# Variable to store the selected time
period_var1 = tk.StringVar()
period_var1.set(period_options[0])  # Set the initial value
hour_var1 = tk.StringVar()
hour_var1.set(hour_options[0])
minute_var1 = tk.StringVar()
minute_var1.set(minute_options[0])

period_var2 = tk.StringVar()
period_var2.set(period_options[0])
hour_var2 = tk.StringVar()
hour_var2.set(hour_options[0])
minute_var2 = tk.StringVar()
minute_var2.set(minute_options[0])

# Labels
hour_label = tk.Label(window, text="Hour:", bg='grey23', fg='white')
hour_label.grid(row=1, column=0, sticky="w", padx=20,pady=10)

minute_label = tk.Label(window, text="Minute:", bg='grey23', fg='white')
minute_label.grid(row=1, column=1, sticky="w", padx=10,pady=10)

period_label = tk.Label(window, text="Period:", bg='grey23', fg='white')
period_label.grid(row=1, column=2, sticky="w", padx=10,pady=10)

# OptionMenus
hour_option_menu1 = tk.OptionMenu(window, hour_var1, *hour_options)
hour_option_menu1.grid(row=2, column=0, sticky="w", padx=20)

minute_option_menu1 = tk.OptionMenu(window, minute_var1, *minute_options)
minute_option_menu1.grid(row=2, column=1, sticky="w", padx=10)

period_option_menu1 = tk.OptionMenu(window, period_var1, *period_options)
period_option_menu1.grid(row=2, column=2, sticky="w", padx=10)

label1 = tk.Label(window, text="  To", fg='white', font=("Arial", 18, "bold"), bg='grey25')
label1.grid(row=3, column=1, sticky="w",pady=20)


hour_option_menu2 = tk.OptionMenu(window, hour_var2, *hour_options)
hour_option_menu2.grid(row=4, column=0, sticky="w", padx=20)

minute_option_menu2 = tk.OptionMenu(window, minute_var2, *minute_options)
minute_option_menu2.grid(row=4, column=1, sticky="w", padx=10)

period_option_menu2 = tk.OptionMenu(window, period_var2, *period_options)
period_option_menu2.grid(row=4, column=2, sticky="w", padx=10)

# Get the color based on the current time
window.configure(background="grey25")

# Start the main event loop
window.mainloop()
