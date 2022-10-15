import tkinter as tk
import random

window = tk.Tk()

# def get_input():
    # name = name_entry.get()
    # output = tk.Label(text="Your Name is "+name)
    # output.pack()

def suffel_number():
    rand_num = random.randint(1, 100)
    num_labls = tk.Entry(text=rand_num, fg="blue", bg="white")
    num_labls.delete()
    num_labls.pack()

label = tk.Label(
    text="Gussing game",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=100,
    height=5
)

button = tk.Button(
    text="Roll",
    width=100,
    height=5,
    bg="Green",
    fg="Black",
    command= suffel_number
)
# name_lable = tk.Label(text="Name")
# name_entry = tk.Entry(fg="black", bg="white", width=115)

# class_lable = tk.Label(text="Class")
# class_entry = tk.Entry(fg="black", bg="white", width=115)



label.pack()
# name_lable.pack()
# name_entry.pack()

# class_lable.pack()
# class_entry.pack()

button.pack()


window.mainloop()