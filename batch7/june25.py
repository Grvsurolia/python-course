# def add():
#     a = 2
#     b = 3
#     print(a + b)

# add()
# add()

#######################

# def add(p, q):
#     print(p + q)

# add(2,3)
# add(11,22)
# add(100,200)

########################
## Void function

# def add(p,q):
#     pass

# print(add(2,3))

#######################

# def add():
#     a = 2
#     b = 3
#     c = a + b
#     return c

# print(add())

#####################

# def multi(a,b):
#     return a*b

# a = 2
# b = 3
# print(multi(a,b))

###################

# name = input("Enter your name: ")

# def hello(name):
#     return "Hello "+name

# print(hello(name))

###################

# name = input("Enter your name: ")

# def hello(name):
#     s = "Hello "+name
#     return s

# print(hello(name))

#########################

# is_odd 
# n 

# input a number 

# Enter a number: 4
# This number is Odd 

# This number is not odd 

# def is_odd(n):
#     if n%2!=0:
#         s = "This number is Odd"
#     else:
#         s = "This number is not Odd"

#     return s

# n = int(input("Enter a number: "))
# # print(is_odd(n))
# check_odd = is_odd(n)
# print(check_odd)


# def is_odd(n):
#     if n%2!=0:
#         print("This number is Odd")
#     else:
#         print("This number is Not Odd")
    
# n = int(input("Enetr a number: "))
# print(is_odd(n))

#################################

# Enter a number or q to stop:
# 2
# Enter a number or q to stop:
# 4
# Enter a number or q to stop:
# 3
# Enter a number or q to stop:
# 6
# Enter a number or q to stop:
# q 
# You have stoped 
# [2,4,3,6]

# n = input("Enter something: ")

# if type(int(n))==int:
#     print("interger")

# if type(n)==int:
#     print("integer")
# elif type(n)==str:
#     print("string")
# elif type(n)==float:
#     print("Float")

# l = []
# while True:
#     n = input("Enter a number or q to stop:\n")
#     if n=="q":
#         print("You have stoped")
#         print(l)
#         quit()
#     else:
#         l.append(n)

############################################
# Enter number of inputs: 4

# Enter a number: 2
# Enter a number: 3
# Enter a number: 4
# Enter a number: 5

# Sum of your values is: 14

# n = int(input("Enter number of inputs: "))
# s = 0
# for i in range(0,n):
#     num = int(input("Enter a number: "))
#     s += num

# print("Sum of your values is:",s)
################################################

# Enter number of inputs: 4

# Enter a number: 22
# Enter a number: 33
# Enter a number: 4
# Enter a number: 55

# Create a function named "minimum"

# Smallest number is 4

##################################################

# l = [2,3,4,4,5,5,6,6,7,7,8,9,1]

# create a function list_length

# Lenth of list = 13

#################################################

# d = {
#     "name1":"Gaurav",
#     "name2":"Anisha",
#     "name3":"Robin"
# }

# Create a function named extract_names

# ["Gaurav", "Anisha", "Robin"]