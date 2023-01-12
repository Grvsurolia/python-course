# def front_back(s):
#     l = list(s)
#     temp = l[0]
#     l[0] = l[-1]
#     l[-1] = temp
#     p = "".join(l)
#     return p

# print(front_back("code"))
# print(front_back("a"))
# print(front_back("ab"))


# s = "gaurav"

# l = list(s)

# l[0] = "s"

# print(l)

# p = "".join(l)

# print(p)

# s = "gaurav surolia"

# l = s.split(" ")

# print(l)


# l = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# print(l[1:-3:3])

############################################################################################################

#### Modules

# 1. User defined Modules
# 2. Pre defined Modules

# from calcy import add, sub, name

# x = 2
# y = 3

# # s = calcy.add(x,y)
# # print(s)

# s = add(x,y)

# # sub = calcy.sub(x,y)
# # print(sub)

# sub = sub()
# print(sub)

# # print(calcy.name)

# print(name)

#####################################################

# from math import sqrt, factorial, pi

# print(sqrt(16))
# print(factorial(5))
# print(pi)

# import math

# print(dir(math))

# print(math.pi)

#################################################################

# import random

# print(random.random())

# print(random.randint(1,6))

# List = [1, 4, True, 800, "python", 27, "hello"]

# print(random.choice(List))

###################################################################

# import datetime

# print(datetime.datetime.now())
# print(datetime.datetime.now().date())

###############################################################

# A = [64, 25, 12, 22, 11]

# for i in range(len(A)):
#     m = i
#     for j in range(i+1, len(A)):
#         if A[j] < A[m]:
#             m = j
    