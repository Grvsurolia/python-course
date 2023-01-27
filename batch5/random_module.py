import random
import tkinter as tk

# print(random.random())
# print(random.randint(1,6))

# l = ["gaurav", "dheeraj", "kamlesh", "salman"]

# print(random.choice(l))
# random.shuffle(l)
# print(l)
# print(dir(random))

# print(random.randint(1,20))

w = tk.Tk()
w.geometry("300x300")

def getValue():
    r = random.randint(1,10)
    entry1.delete(0, r)
    entry1.insert(0,r)
    lable1 = tk.Label(w,text = r)
    lable1.pack()

entry1 = tk.Entry(w)
entry1.pack()

btn1 = tk.Button(text="Change", command=getValue)
btn1.pack()


w.mainloop()