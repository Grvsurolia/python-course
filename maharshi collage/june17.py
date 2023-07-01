## Scope of a function

# a = 3       # Global Variable
# def first(a):
#     print(a)
#     a = 2       # Local Variable
#     print(a)

# print("Bahar = ",a)
# first(a)

#################################

# def str_break(s):
#     print(list(s))

# str_break("Programming")

# s = "Programming"
# ["P","r","o","g","r","a","m","m","i","n","g"]

#################################

# class Calculator 
# fun add 
# fun sub 
# fun multi 
# fun div 

# Enter first no: 10
# Enter second no: 5
# Enter Symbol: +
# Add = 15

# class Calculator:
#     def add(self, a, b):
#         print("Add = ",a+b)
#     def sub(self, a,b):
#         print("Subtract = ",a-b)
#     def multi(self, a,b):
#         print("Multiply = ",a*b)
#     def div(self, a, b):
#         print("Divide = ",a/b)

# p = int(input("Enter first no: ")) 
# q = int(input("Enter second no: "))
# c = input("Enter symbol +, - , * , /: ")

# ob = Calculator()

# if c=="+":
#     ob.add(p,q)
# elif c=="-":
#     ob.sub(p,q)
# elif c=="*":
#     ob.multi(p,q)
# elif c=="/":
#     ob.div(p,q)
# else:
#     print("Invalid Symbol")

###########################################

# class Student
# fun details
# fun marks

# name 
# age 

# python marks 
# Maths marks 

# Output:
# Your Name is Gaurav
# Your age is 2

# Your python marks is 88
# Your Maths marks is 99

# class Student:
#     def details(self, name, age):
#         print("Your Name is ",name)
#         print("Your Age is ",age)
#     def marks(self, m1, m2):
#         print("Your Python marks is ",m1)
#         print("Your Maths marks is ",m2)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# m1 = int(input("Enter Python marks: "))
# m2 = int(input("Enter Maths marks: "))

# ob = Student()
# ob.details(name, age)
# ob.marks(m1,m2)