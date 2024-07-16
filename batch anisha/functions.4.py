############## Closers

# def first():
#     print('first function')
#     def second():
#         print("Second function")
#         def third():
#             print("Third function")
#         third()
#     second()
# first()

###################### Variable arguments

# def add(a,b):
#     return a+b

# add(2,3)

# n = int(input('Enter number of elements: '))
# l = []
# for i in range(n):
#     e = input("Enter Element: ")
#     l.append(e)
# print(l)
#####################   ARGS
# def add(*arg):
#     # print(arg, type(arg))
#     for i in arg:
#         print(i)

# add(11,22,33,44,55,66,77,88,99)
####################    kwargs

# def getValues(**kwargs):
#     print(kwargs)
#     # print(type(kwargs))
#     for k,v in kwargs.items():
#         print(k,"=",v)


# getValues(name="Gaurav",class_=2,age=5,class_teacher="Miss Pooja")

##########################################################

