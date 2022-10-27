# def add(a,b,c=0):   # c=0 -> Default value
#     return a+b+c

# print(add(2,3))

# print(add(2,3,4))

#####################################################################

# class First:
#     def __init__(self,a,b):
#         print("first")
#         self.a = a
#         self.b = b
    
#     def add(self):
#         print(self.a + self.b)

# class Second:
#     def __init__(self,a,b,c):
#         print("second")
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def add(self):
#         return self.a + self.b + self.c

# ob1 = First(2,3)

# ob1.add()

# ob2 = Second(2,3,4)

# print(ob2.add())


##############################################################################

# def last2(str):
#     count = 0
#     last = str[-2:]
#     for i in range(0,len(str[:-2])):
#         if str[i] + str[i+1] == last:
#             count += 1
#     return count 

# print(last2("axxxaaxx"))

###########################################################################


# l = [2,4,6,8,10,12,14,16,18,20,22]

# print(l[:10:3])