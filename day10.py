#### Return a function

# def add(a, b):
#     return a + b


# x = add(2,3)
# y = add(5,6)

# print(x, y)
####################################################################################################

#### Map Function

## SYNTEX

# map(function, iterator)

# def p(a):
#     return a * 2

# print(tuple(map(p, [2,3,4,5,6,7,8,9])))

# def add(a,b):
#     return a + b

# print(list(map(add, [1,2,3,4,5,6,7,8,9],[1,3,5,7,2,4,3,5,3])))

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 20

# [1,4,9,16,25,36,49,64,81,400]

# def user_input(i):
#     m = int(input("Enter a number: "))

#     return m * m

# print(list(map(user_input, range(0,10))))










############################################################################################

# def square(a):
#     return a ** 2

# l = []

# for i in range(10):
#     m = int(input('enter a number: '))
#     l.append(m)

# print(list(map(square, l)))
#############################################################################################
# def user_input(i):
#     m = int(input("Enter a number: "))
#     return m ** 2

# print(list(map(user_input, range(0,10))))

##############################################################################################

# user 10 int input
# list 

# 10 -> Hello 10

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 20

# [1,2,3,4,5,6,7,8,9,20]
# Hello 1
# Hello 2
# .
# .
# .
# .
# .
# Hello 20


# def first(i):
#     m = int(input("Enter a number: "))

#     return "hello "+ str(m)

# l = list(map(first, range(0,10)))

# for i in l:
#     print(i)

###########################################################################################################

# l = [11,22,33,4,55,66,77,11,99,100]

# n = int(input("Enter a number: "))

# if n in l:
#     print("Yes")
# else:
#     print("No")

# p = False

# for i in range(0,len(l)):
#     print(n, l[i])
#     if n == l[i]:
#         p = True

# print(p)


#########################################################################################################

# n = 368

# output
# 863

####################################################################################################################

