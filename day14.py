#### Inharitance

## SYNTEX

# Derived Class
# Base Class



# class parent:
#     statement 

# class child(parent):
#     statement 

#####################################################################



# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def circumference(self):
#         return 2*3.14*(self.radius)
    
#     def areaOfCircle(self):
#         return 3.14 * (self.radius**2)

# # c = Circle(3)

# # print(c.circumference())

# # print(c.area())

# class Call(Circle):
#     def __init__(self, a,b):
#         Circle.__init__(self,3)
#         self.a = a
#         self.b = b

# c = Call()

# print(c.circumference())
# print(c.areaOfCircle())


#################################################################################################################


## Exception Handling

# try:
#     n = int(input("Enter a number: "))
#     print(n)
# except:
#     print("Please enter a number only")

# try:
#     n = int(input("Enter a number: "))
#     print(n)
# except Exception as e:
#     print(e)

############################################################# 
# try:
#     a = 2
#     b = 0
#     print(a/b)
# except Exception as e:
#     print("Can not divide by zero\n",e)