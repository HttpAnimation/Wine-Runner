import tkinter as tk
from tkinter import filedialog
import subprocess

def run_file():
    # Get the path to the executable file
    file_path = filedialog.askopenfilename(filetypes=(("Executable files", "*.exe;*.msi"), ("All files", "*.*")))
    
    # Check if the path is not empty
    if file_path:
        # Check if --no-sandbox option is selected
        if sandbox_var.get() == 1:
            wine_cmd = ['wine', '--no-sandbox', file_path]
        else:
            wine_cmd = ['wine', file_path]
        
        # Run the executable file with Wine using subprocess
        subprocess.Popen(wine_cmd)
        
# Create the main window
window = tk.Tk()
window.title("Wine Runner")
window.geometry("300x150")

# Create a label and button to select the executable file
file_label = tk.Label(window, text="Select an EXE or MSI file:")
file_label.pack()

file_button = tk.Button(window, text="Browse", command=run_file)
file_button.pack()

# Create a checkbox for the --no-sandbox option
sandbox_var = tk.IntVar()
sandbox_check = tk.Checkbutton(window, text="Add --no-sandbox", variable=sandbox_var)
sandbox_check.pack()

# Start the main event loop
window.mainloop()
