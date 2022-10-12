# phone_no = input("Enter your number")

# check = False
# try:
#     for i in phone_no:            
#         a = int(i)
# except:
#     check = True 

# first_list = [7,8,9]

# if len(phone_no) != 10:
#     print("Number should be of 10 digit")
# elif int(phone_no[0]) not in first_list:
#     print("Number should start from 7, 8 or 9")
# elif check == True:
#     print("Only Numbers are Allowed")
# else:
#     print(phone_no)

#########################################################################

# a = 2
# b = 4
# c = 7

# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# ######################################################################################################################

# ### GENERATORS

# def first(a,b):
#     return a+b 

# x = first(2,4)

# print(x)

# def AddToNumberToReturnsOMTHING():
#     yield 1
#     yield 2
#     yield 3

# add = AddToNumberToReturnsOMTHING()

# # print(add)

# # for i in add:
# #     print(i)
# try:
#     next(add)
#     next(add)
#     print(next(add))
#     print(next(add))
# except:
#     print("No more values")

#################################################################################################

#### ANY / ALL

# ANY - or

# print(any([False, False, True, False]))

# print(False or False or True or False)

# ALL - AND 

# print(True and True and False)

# print(all([True, True, True]))


# list1=[2,3,4,5,8,44,66]
# odd_list=[]

# for i in list1:
#     if i % 2 != 0:
#         odd_list.append(True) 
#     else:
#         odd_list.append(False)       

# print(odd_list)

# print(any(odd_list))

# if any(odd_list):
#     print("Odd number is present")
# else:
#     print("nO ODD NO FOUND")

#############################################################################################################


# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end="")
#     print()

###################################################################################################################

# *****
# ****
# ***
# **
# *

###################################################################################################################

#     *
#    * *
#   * * * 
#  * * * *
# * * * * *

####################################################################################################################

# n = 1234

# while(n % 10 != n):
#     n = n//10
# print(n)