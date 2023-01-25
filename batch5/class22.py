# ##### Constructor

# class First:

#     def __init__(self, a,b):
#         self.a = a
#         self.b = b

#     def add(self):
#         return self.a+self.b

#     def multi(self):
#         return self.a * self.b

# ob = First(2,3)

# a = ob.add()
# print(a)


# class Second:

#     def p():
#         print("hello")

# ob2 = Second()

#####################################

# class Student:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         # print("Hello "+self.name)
#         return "Hello "+self.name
    
#     def print_age(self):
#         # print("Your age is",self.age)
#         return "Your age is"+str(self.age)

# stu1 = Student("Dheeraj", 26)
# stu2 = Student("Kamlesh", 21)
# stu3 = Student("Anurag", 19)

# print(stu1.greet() + stu1.print_age())
# stu2.greet()
# stu2.print_age()
# stu3.greet()
# stu3.print_age()

##########################################################

####### INHARITANCE

# class Parent:

#     def __init__(self, car, house):
#         self.car = car
#         self.house = house

#     def total_property(self):
#         return self.car + self.house
    
#     def names(self, m_name, f_name):
#         return [m_name, f_name]

# # p = Parent(20000000, 5000000000)

# # print(p.total_property())

# # print(p.names("sita", "Ram"))

# class Child(Parent):
#     def my_property(self, n):
#         return self.total_property()/n

# c1 = Child(20000000, 5000000000)

# print(c1.total_property())

# print(c1.names("Sita", "Ram"))

# c2 = Child(20000000, 5000000000)

# print(c2.total_property())

# print(c2.names("Sita", "Ram"))

# print(c2.my_property(2))


#################################################################

# stu1 = {
#     "name":"dheeraj",
#     "class":2,
#     "roll_no":7
# }

# stu2 = {
#     "name":"kamlesh",
#     "class":3,
#     "roll_no":8
# }

# [("dheeraj", 2, 7),("Kamelsh",3,8)]
# l = [stu1,stu2]

# output = []

# for stu in l:
#     l2 = []
#     for k,v in stu.items():
#         l2.append(v)
#     output.append(tuple(l2))

# print(output)


#####################

stu1 = {
    "name":"dheeraj",
    "class":2,
    "roll_no":7
}

stu2 = {
    "name":"kamlesh",
    "class":3,
    "roll_no":8
}

def convert_into_list(stu):
    l2 = []
    for k,v in stu.items():
        l2.append(v)

    return tuple(l2)

m = map(convert_into_list, [stu1,stu2])

print(list(m))

