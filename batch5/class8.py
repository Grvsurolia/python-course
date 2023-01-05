###### Break and Continue

## Break


# for i in range(11):
#     if i==6:
#         break
#     print(i)

## Continue

# for i in range(11):
#     if i>5 and i<9:
#         continue
#     print(i)


###################################################################

#### Containers

# List ( list )
# Tuple ( tuple )
# Set (set)
# Dictionary (dict)

##### List

# l = [2,3,4,5,"p",6,7,2.22, 6.66,87,9, "a",3.14]

# print(l)

# print(type(l))

# print(len(l))

# print(l[0])
# print(l[4])
# print(l[8])

# print(l[-2])

# print(l[-7])

###### Slicing

# l = [2,3,4,5,"p",6,7,2.22, 6.66,87,9, "a",3.14]

# print(l[0:4])
# print(l[:4])

# print(l[-5:])

# print(l[0::2])

# print(l[::-1])

###### Tuple

# t = (2, 3, 4, 5, 6, "p", 3.15, 55)

# print(t)
# print(type(t))

# print(t[0])
# print(t[5])

# print(t[-2])

# print(t[1:5])

########### Diffrence B/w List and Tuple

# List: mutable
# Tuple: Immutable

# t = (1,2,3,4,5,6,7,8,9)
# l = [1,2,3,4,5,6,7,8,9]


# l[0] = 11
# print(l)

# t[0] = 11
# print(t)

# t = (1,2,3,4,[5,6,7],8,9)
# print(len(t))

# print(t[3])
# print(t[4][1])

# t[4][0] = 55
# print(t)

########### 

# l = [2,4,6,8,10,......20]

# [22,44,66,88,1010,........ 2020]