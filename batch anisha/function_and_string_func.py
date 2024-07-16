# txt = "Hello SamSam!"
# mytable = str.maketrans("SHm", "Pet")
# print(mytable)
# print(txt.translate(mytable))

# print(txt.replace("Shm", "Pet"))

# point = {'x':4,'y':-5, 'z': 0}
# print('{y} {x} {z}'.format_map(point))

# a = "22.5"

# print(a.isdecimal())
# print(a.isdigit())
# print(a.isnumeric())

##########################################################################

######################### Lambda Function 

# def add(a,b):
#     return a+b

# Single lined function, multiple arguments, single return 

##### SYNTEX 

# functionName = lambda arguments: statement 

# add = lambda a,b : a+b

# c = add(2,3)
# print(c)

# sq = lambda a : a ** 2

# print(sq(8))

#########################################################################

############## Scope of a function 

# local 
# Global 

# a = 3

# def first(a):
#     print("inn 111",a)
#     a = 2
#     print("Innn 222",a)

# def second(a):
#     a = 5
#     print("seccccccc ",a)

# first(a)
# print("out",a)
########################
# def first():
#     a = 2
#     print("first = ",a)

#     def second(a):
#         a = 3
#         print("second = ",a)
#     second(a)
#     print("firstttttt",a)

# first()
####################################################

############ Function Documentation

# def add(a,b):
#     """This function add 2 numbers."""
#     return a+b

# add()

#### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

