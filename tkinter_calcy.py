import tkinter as tk

window = tk.Tk()

window.geometry("400x500")

def calculate():
    entry_no_value = enter_number.get()
    output = eval(str(entry_no_value))
    out = tk.Label(text=output)
    out.pack()

heading = tk.Label(text="Calculator")
enter_number = tk.Entry()
equals_to_button = tk.Button(text="=", command=calculate)

heading.pack()
enter_number.pack()
equals_to_button.pack()

window.mainloop()