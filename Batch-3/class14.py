# a = int(input("Enter first no.: "))
# b = int(input("Enter second no.: "))
# symbol = input("Enter Symbol: ")

# def add(x,y):
#     return x+y

# def subtract(x,y):
#     return x-y

# def multipy(x,y):
#     return x*y

# def divide(x,y):
#     return x/y

# if symbol=="+":
#     print(add(a,b))
# elif symbol=="-":
#     print(subtract(a,b))
# elif symbol=="*":
#     m = multipy(a,b)
#     print(m)
# elif symbol=="/":
#     d = divide(a,b)
#     print(d)
# else:
#     print("Please Enter valid symbol")

###################################################################################

# def a():
#     b = 2
#     return b

# print(a())

###################################################################################

# def takeInput():
#     return input("Enter Something: ")

# l = []

# for i in range(10):
#     a = takeInput()
#     l.append(a)

# print(l)

###################################################################################

# name = input("Enter your Name: ")

# def splitName(name):
#     l = []
#     for i in name:
#         l.append(i)
#     return l

# name_list = splitName(name)
# print(name_list)

################################################################################

# n = int(input("Enter no.: "))

# a = 1

# if n==0:
#     a = 0
# else:
#     for i in range(1,n+1):
#         a = i * a

# print(a)

#############################################################################

## Recursion

# n = int(input("Enter no.: "))

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         print(n)
#         return n * factorial(n-1)

# f = factorial(n)
# print(f)

#################################################################################

# n = int(input('Enter No. : '))

# def add(n):
#     if n==0:
#         return 0
#     else:
#         return n + add(n-1)

# a = add(n)
# print(a)