import tkinter as tk

# Initialize the tkinter root widget, which builds a window.
root = tk.Tk()

w = tk.Label(root, text="Hello world!")

# Fit the window to the given content.
w.pack()

# Enter the tkinter event loop.
root.mainloop()