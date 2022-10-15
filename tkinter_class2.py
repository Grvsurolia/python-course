import tkinter as tk
import random

window = tk.Tk()

def random_no():
    r_num = random.randint(1,100)
    text_lable = tk.Label(text=r_num)
    text_lable.pack()

label = tk.Label(
    text="Gussing game",
    foreground="white",  
    background="black",
    width=100,
    height=5
)

button = tk.Button(
    text="Roll",
    width=100,
    height=5,
    bg="Green",
    fg="Black",
    command=random_no
)

button.pack()
label.pack()

window.mainloop()