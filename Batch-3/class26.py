#### Iterators in Python

# l = [2,3,4,5,6,7,8,9,10]

# i = iter(l)

# try:
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))
#     print(next(i))

# except (ZeroDivisionError,StopIteration):
#     print("Done")

###############################################################

# l = [2,3,4,5,56,7,88,9,90,0,8]

# i = iter(l)

# for j in range(len(l)):
#     print(next(i))

#############################################################

##### Generators in Python

# def func(a,b,c,d):
#     yield a
#     yield b
#     yield c
#     yield d

# ob = func(2,3,4,5)
# try:
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
#     print(next(ob))
# except:
#     print("No more values to Iterate")


# def func(l):
#     for i in l:
#         yield i

# ob = func([2,3,4,5,6,7,8,9,10])

# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))
# print(next(ob))

###########################################################

# def func(a):
#     return a

# ob = func(3)

# print(ob)
