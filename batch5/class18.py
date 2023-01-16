# def return_list(l=[]):
#     for i in range(5):
#         n = input("Enter something: ")
#         l.append(n)
#     return l

# print(return_list())

######################################################

## default args

# def add(a=33,b=44):
#     return a+b

# a = add(2,4)
# print(a)

########################################################

## Scope of a variable

# 1. Global variable
# 2. Local Variable

# a = 2       # Global variable

# def first(a):
#     a = 3       # Local Variable
#     return a

# f = first(a)

# print(f)

##############################################################

## Function Documentation

# def add(a,b):
#     """
#     This function is adding two numbers
#     return a+b
#     """
#     return a+b

# print(help(add))

##########################################################

#### Lambda function

# def add(a,b):
#     a = a+2
#     b = b+2
#     return a+b

### syntex
# functionname = lambda agrs1, args2,...... : expression

# 1. Multiple Arguments
# 2. return 1 expression

# add = lambda a,b:a+b

# a = add(2,5)
# print(a)

#######################################################

a = 2