###### mutable & Immutable

l = [1,2,3,4]
# l.append(5)

# print(l)

# t = (1,2,3,4)

# t[1] = [5,6,7,8]

# print(t)

# s = {1,2,3}
# p = {4,5,6}

# p.update([2.3,44,55,66])
# print(p)

# print(s[0])

# t = (2,3,4)

# l = [5,6,7]

# Student = {"name": "Ankit", "age": 21, "sex": "Male",
#            "college": "MNNIT Allahabad", "address": "Allahabad"}

# for k, v in Student.items():
#     print(k,v)

# s = set(Student)
# print(s)

# dice = ["1","2","3","4","5","6"]

# print(set(dice))

############################################

# l = [2,3,4,5,6,6,6,4,3,3,4,8,6,5,4,3,3,33,4,5,67,7,87,8,5]

# p = []

# print(len(l))

# if len(l)%2==0:
#     for i in range(0,len(l),2):
#         add = l[i] + l[i+1]
#         p.append(add)
# else:
#     for i in range(0,len(l)-1,2):
#         add = l[i] + l[i+1]
#         p.append(add)
#     p.append(l[-1])
# print(p)

##################################################################

# l = [111,222,333,444,555,666,777,888,999]

# even = []
# odd = []

# for i in l:
#     if i%2==0:
#         even.append(i//10)
#     else:
#         odd.append(i//100)

# print(even)
# print(odd)

###########################################################

# l = [111,222,333,444,555,666,777,888,999]

# [222,111,444,333,666,555,888,777,999]

#############################################################

### Input

# a = 22
# b = 44

### output 

# before swap
# a = 22
# b = 44

# after swap
# a = 44
# b = 22

#### M1 
# print(a,b)

# c = a
# a = b
# b = c

# print(a,b)

## M2
# print(a,b)

# a = a + b
# b = a - b 
# a = a - b

# print(a,b)

## M3

# print(a,b)

# a,b = b,a

# print(a,b)

# a = 2
# b = 3
# c = 4

# a,b,c = 2,3,4

# print(a)
# print(b)
# print(c)
