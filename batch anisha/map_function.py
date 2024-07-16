############### MAP FUNCTION

l = [1,2,3,4,5,6,7,8,9]

# for i in range(len(l)):
#     l[i] = l[i] * 10

# print(l)

# def multi10(i):
#     return i * 10

# m = tuple(map(multi10, l))
# print(m)

# m = list(map(lambda i:i*10, l))
# print(m)

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# Enter 5 numbers:
# 22
# 33
# 44
# 55
# 66

# sum is ****

# print("Enter 5 numbers comma seprated: ")
# l = list(map(int, input().split(",")))
# print(l)

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# l = [2,3,4,5,6]
# Enter element to search: 22

# Not found 

# Found 

# print("Enter 5 numbers comma seprated: ")
# l = list(map(int, input().split(",")))
# print(l)

# f = int(input("Enter number: "))

# def isFound(i):
#     if i==f:
#         return True
#     else:
#         return False

l = list(map(isFound, l))
print(l)
print(any(l))


######################### ALL and ANY

# l = [True, False, False, False, True]

# print(all(l))
# print(any(l))

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# INPUT:  [100,200,300,400,500,600,700,800]

# OUTPUT: {1:100, 2:200, 3:300...............}

# l = [100,200,300,400,500,600,700,800]

# def convertDict(i):
#     return i//100,i

# print(dict(map(convertDict, l)))

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# Input: [(1,2),(2,3),(3,4),(4,5),(5,6)]

# Output 1: [1,2,2,3,3,4,4,5,5,6]

# Output 2: [1,2,3,4,5,6]

l = [(1,2),(2,3),(3,4),(4,5),(5,6)]

l2 = list(map(lambda x:x[0], l)) + list(map(lambda x:x[1], l))
l2.sort()
print(l2)

# l3 = []
# def isInList(i):
#     if i not in l2:
#         l2.pop(i)

# print(map(lambda x:x))