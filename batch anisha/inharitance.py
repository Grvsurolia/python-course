####################### INHERITANCE

# Class which inharit the properties of another class 

# where Child (BASE) class inhErit the properties of parent (InhErited) class 

# class First:
#     a = 2
#     b = 3

# class Second(First):
#     c = 4
#     d = 5

#     a = 11

# ob1 = First()
# ob2 = Second()

# print(ob1.a)
# print(ob1.b)
# print(ob2.c)
# print(ob2.d)
# print(ob2.a)

###########################################################

# class Parent:
#     f_name = "Ram"
#     m_name = "Sita"

#     def bankBalance(self):
#         return 5500000000
    
#     def has_car(self):
#         return "Yes"
    
# class Child(Parent):
#     name = "Chintu"

#     def bankBalance(self):
#         return 100000 + super().bankBalance()
    
#     def has_car(self):
#         if super().has_car()=="Yes":
#             return "Yes"
#         else:
#             return "No"
    
# pOb = Parent()
# cOb = Child()

# print(cOb.bankBalance())
# print(cOb.has_car())

#######################################

# a = 22

# if a==2:
#     print("Yessssssssss")
# else:
#     print("Noooooooooooo")

# print("Yesssss" if a==2 else "Noooooo")

##################### TYPES OF INHERITANCE

# SINGLE INHERITANCE
# MULTIPLE INHERITANCE
# MULTILEVEL INHERITANCE
# HYBRID INHERITANCE
# HIERARICHAL INHERITANCE

################################

# MULTIPLE INHERITANCE

class A:
    print("AAAAAAAAAAAAAAAA")
    a = 2

class B:
    print("BBBBBBBBBBBBBBBB")
    b = 3

class C(A,B):
    c = 4

# cOb = C()
# print(cOb.a)
# # print(cOb.b)
# print(cOb.c)

##### MULTILEVEL INHERITANCE

# class A:
#     a = 2

# class B(A):
#     b = 3

# class C(B):
#     c = 4

# class D(C):
#     d = 5

# bOb = B()
# print(bOb.a)
# print(bOb.b)

# dOb = D()
# print(dOb.a)
# print(dOb.b)
# print(dOb.c)
# print(dOb.d)

###################################
