######## Classes

# class Class1:
#     a = 22
#     b = 33
#     c = 44

#     def func1(self,a,b,c):
#         return a+b+c

# ob1 = Class1()
# ob2 = Class1()
# print(ob1)
# print(ob2)
# print(ob1.a)

# print(Class1().func1())

########## Constructor

# class Class2:
#     def __init__(self, name):
#         self.name = name

#     def func2(self, age):
#         return "Hello "+self.name+" Your Age is "+str(age)
    
#     class C2:
#         a = 22

# ob1 = Class2("gaurav")
# ob2 = ob1.C2()
# print(ob2.a)


# ob1 = Class2("gaurav")
# print(ob1.func2(22))

# ob2 = Class2("Dheeraj")
# print(ob2.func2(33))


#################### Polymorphism

# class Class1:

#     def hello(self):
#         return "Hello"
    
#     def add(self,a,b):
#         return a+b
    
# class Class2:
    
#     def hello(self):
#         return "Hello Gaurav"
    
#     def add(self,a,b,c=10):
#         return a+b+c


# ob1 = Class1()
# ob2 = Class2()

# print(ob1.hello())
# print(ob2.hello())

# print(ob1.add(2,3))
# print(ob2.add(2,3))

##############################################

###### Data Abstraction

# def add(a,b):
#     print(a+b)

# def sub(a,b):
#     print(a-b)
