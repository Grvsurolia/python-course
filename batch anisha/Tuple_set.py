####### Tuple

# t1 = (1,2,3,4,5,6,6,6,7,7,8,9)
# print(t1)

### Immutable: Can not modify

# c = t.count(6)
# print(c)

# i = t.index(5)
# print(i)

# t2 = (11,22,33,44,55,66)
# t1 = t1+t2
# print(t1)

########## SET

s = {11,2,3,4,4,5,5,6,116,6,77,7,8,8,9}
print(s)
# p = {11,2,3,4,4,5,6,67,8,9}
## carry unique elements, unordered, sorted

# s.add(111)
# s.add(222)
# print(s)

# print(s.difference(p))

# s.clear()
# print(s)

# s2 = set()
# print(s2, type(s2))

# s2 = s.copy()
# print("s2 = ",s2)
# s.add(222)
# print(s)
# print(s2)

# s2 = s
# print("s2 = ",s)
# s.add(222)
# print(s)
# print(s2)

# s2 = {2,3,4}
# s.difference_update(s2)
# print(s)


#########################################################

####################### CONVERSIONS
### LIST to TUPLE

# l = [1,2,3,4,5,5,5]
# t = tuple(l)
# print(t)

### LIST to SET

# s = set(l)
# print(s)

### tuple to list
# t = (1,2,3,4,5,5,6)

# l = list(t)
# print(l)

## tuple to set

# s = set(t)
# print(s)

### set to list

# s = {1,2,3,4,5,5,6,6,7}
# print(s)

# l = list(s)
# print(l)

# ### set to tuple
# t = tuple(s)
# print(t)

#### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# t = (11,22,33,44,55,66,77,88)

# output: (11,22,33,44,55,66,77,88,99)
# do not create any extra tuple

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# t = (11,22,33,44,55,55,66,66,77,88,88)

# Output: (11,22,33,44,55,66,77,88)

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# Take a string input from user 
# convert each char to list, except space

# s = "I love programming"

# print(list(s))

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# l = ["anisha", "gaurav", "ram", "shyam", "sita"]
# output: [2,2,1,1,1]

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# l = ["anisha", "gaurav", "ram", "shyam", "sita"]
# output: [6,6,3,5,4]

###################################################################

