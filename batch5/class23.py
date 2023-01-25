# s = "aAbBcCdDeEfFgGhHiI"

# p = ""

# for i in s:
#     if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I":
#         p += i

# l = ["a","e","i","o","u","A","E","I","O","U"]

# for i in s:
#     if i in l:
#         p += i


# print(p)

#################################################################


##### Types of Inharitance

# Single Inharitance

# class A:

#     a = 2
#     def funcA(self):
#         print("AAAAAAAAAAAAAAa")

# class B(A):
#     pass

# aOb = A()
# aOb.funcA()

# bOb = B()
# bOb.funcA()

######################

# Multiple Inharitance

# class A:

#     def funcA(self):
#         print("AAAAAAAAAAAAAAAAAAaa")

# class B:

#     def funcB(self):
#         print("BBBBBBBBBBBBBBbbbbbbbbbb")


# class C(A,B):

#     def funcC(self):
#         print("CCCCCCCCccccccccccccccc")


# aOb = A()
# bOb = B()
# cOb = C()

# aOb.funcA()

# bOb.funcB()

# cOb.funcA()
# cOb.funcB()
# cOb.funcC()

################################################################

######## MULTI LEVEL INHARITANCE

# class A:

#     def Khet(self):
#         print("5000000000")


# class B(A):

#     def house(self):
#         print("2000000000")


# class C(B):

#     def Knowledge(self):
#         print("Python")

# aOb = A()
# bOb = B()
# cOb = C()

# aOb.Khet()
# bOb.house()
# bOb.Khet()

# cOb.Knowledge()
# cOb.house()
# cOb.Khet()

#########################################

##### Hierarchical Inheritance

# class A:

#     def funcA(self):
#         print("AAAAAAAAAAAAAAaaAAaa")

# class B(A):
#     pass

# class C(A):
    
#     def funcC(self):
#         print("CCCCCCCCCCCCCCCCCCC")

# class D(A):

#     def funcD(self):
#         print("DDDDDDDDDDDDDDD")

    

# aOb = A()
# bOb = B()
# cOb = C()
# dOb = D()

# aOb.funcA()

# bOb.funcA()

# cOb.funcA()

# dOb.funcD()
# dOb.funcA()