import tkinter as tk

width = 3
height = 3

root = tk.Tk()
root.title("Tic tac toe")

for i in range(height):
    for j in range(width):
        label = tk.Label(root, padx = 40, pady = 10, text="X")
        label.grid(row=i)

root.mainloop()