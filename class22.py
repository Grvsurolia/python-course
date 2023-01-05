##### Inharitance

class First:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def func(self):
        print("a = ",self.a)
        print("b = ",self.b)

ob = First(2,3)

ob.func()

class Second(First):
    def func2(self):
        print(self.a + self.b)

ob2 = Second(22,33)

ob2.func()

ob2.func2()

