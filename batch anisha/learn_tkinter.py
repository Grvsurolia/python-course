# import tkinter as tk

# def do_print():
#     print("Helooooooooooooo")
#     label = tk.Label(wn, text="hello")
#     label.pack()

# wn = tk.Tk()

# wn.title("First App")

# wn.geometry("800x500")

# label = tk.Label(wn, text="Wellcome!").grid(row=0,column=0)
# # label.pack()

# button = tk.Button(wn, text="Click here", command=do_print).grid(row=1,column=1)
# # button.pack()

# ent = tk.Entry(wn).grid(row=2,column=2)
# # ent.pack()

# wn.mainloop()

# from tkinter import *

# root = Tk()
# root.title('GfG')
# top = Toplevel()
# top.title('Python')
# top.mainloop()


##################################################

import tkinter as tk

wn = tk.Tk()

wn.title("Calculator")
wn.geometry("400x300")

display = tk.Entry(wn, width=20).grid(row=0, column=0, columnspan=3)

def btn_click(value):
    text = display.get()
    print(text)

btn = tk.Button(wn, text="0", width=5, height=2, command=btn_click("0")).grid(row=1,column=0)
btn = tk.Button(wn, text="1", width=5, height=2).grid(row=1,column=1)
btn = tk.Button(wn, text="2", width=5, height=2).grid(row=1,column=2)
btn = tk.Button(wn, text="3", width=5, height=2).grid(row=2,column=0)
btn = tk.Button(wn, text="4", width=5, height=2).grid(row=2,column=1)
btn = tk.Button(wn, text="5", width=5, height=2).grid(row=2,column=2)
btn = tk.Button(wn, text="6", width=5, height=2).grid(row=3,column=0)
btn = tk.Button(wn, text="7", width=5, height=2).grid(row=3,column=1)
btn = tk.Button(wn, text="8", width=5, height=2).grid(row=3,column=2)
btn = tk.Button(wn, text="9", width=5, height=2).grid(row=4,column=0)
btn = tk.Button(wn, text="+", width=5, height=2).grid(row=4,column=1)
btn = tk.Button(wn, text="-", width=5, height=2).grid(row=4,column=2)
btn = tk.Button(wn, text="*", width=5, height=2).grid(row=5,column=0)
btn = tk.Button(wn, text="/", width=5, height=2).grid(row=5,column=1)
btn = tk.Button(wn, text="=", width=5, height=2).grid(row=5,column=2)

wn.mainloop()