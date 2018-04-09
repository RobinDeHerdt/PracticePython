import tkinter as tk

counter = 0

def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(1000, count)

    # Start the recursive function
    count()


root = tk.Tk()

root.title("Counter")

# Set the initial label, which has no value (yet).
label = tk.Label(root, fg="red")
label.pack()

counter_label(label)

button = tk.Button(root, text='Stop counting', width=25, command=root.destroy)
button.pack()

root.mainloop()