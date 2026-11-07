# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup tkinter window
root=Tk()
root.geometry("200x200")

# function for displaying warning message
# This will be called when the button is clicked
# messagebox.showwarning("Window name","text to be displayes")
def msg():
    messagebox.showwarning("Alert","stop! virus found.")

# Adding button widget to window
button=Button(root, text="Scan for virus",command=msg)
button.place(x=40,y=80)

# Entering main event loop
root.mainloop()