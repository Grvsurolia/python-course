### Maximum of a list

# l = [4,7,2,99,108,7,8,999,1,10,55,33,22,89]

# def maximum(l):
#     m = l[0]

#     for i in l:
#         print("m = ",m, "i = ", i)
#         if m < i:
#             m = i


# maximum(l)

# print(max(l))

# print(min(l))



######## SCOPE of a variable in python

## 1. Local variable
## 2. Global variable

# a = 2     ## Global variable
# def first():
#     a = 5   ## Local variable
#     print("inner = ",a)

# first()

# print("outer = ",a)

### Break and Continue

# list1 = [1,2,3,4,5,6,7,8,9,10,11,22,33,44,55,6,77,88,99,100]

# for i in list1:
#     if i >= 11:
#         break
#     print(i)


# for i in list1:
#     if i >= 11:
#         continue
#     print(i)


# l = [1,3,4,6,3,7,5,9,6,2,4]

## [1,3,4,6,7,5,9,2]

# print(list(set(l)))


# l = [1,3,4,6,3,7,5,9,6,2,4]


dict1 = {
    "mahipal": {
        "class":2,
        "dob":"5/11/2002",
        "course":"python"
    },
    "komal":{
        "class":10,
        "dob":"10/5/2003",
        "course":"python"
    }
}

# print(dict1["komal"]["class"])

# [ ["mahipal", 2 , "5/11/2002", "Python"], ["komal", 10, "10/5/2003", "Python"] ] 

# print(list(dict1))
# m = []

# for i in dict1:
#     l = []
#     print("i = ",i)
#     print("dict1[i] = ",dict1[i])
#     l.append(i)
#     for j in dict1[i]:
#         print("j = ",j)
#         print(dict1[i][j])
#         l.append(dict1[i][j])
#     m.append(l)

# print(m)

# d = {
#     "a": 1,
#     "b": {
#         "aa":11,
#         "bb":22
#     },
#     "c":{
#         "cc":33,
#         "dd":44
#     }
# }

# print(d["b"]["aa"])



# dict1 = {
#     "mahipal": {
#         "class":2,
#         "dob":"5/11/2002",
#         "course":"python"
#     },
#     "komal":{
#         "class":10,
#         "dob":"10/5/2003",
#         "course":"python"
#     }
# }

# m = []

# for k, v in dict1.items():
#     l = []
#     l.append(k)
#     for i, j in v.items():
#         l.append(j)
#     m.append(l)

# print(m)

# d = {"name":"Gaurav", "class": "10", "course":"python"}

# for key, value in d.items():
#     print(key)
#     print(value)

# {"Gaurav":"name", "10":"class", "python":"course"}

# o = {}

# for k, v in d.items():
#     o[v] = k

# print(o)

# list1 = [2,3,4,55,66,77,2,34,5,68,8,9,3,1]

# userInput = int(input("Enter a number: "))

# if n in l:
#     print("yes")
# else:
#     print("No")

# isPresent = False

# for i in list1:
#     if i==userInput:
#         isPresent = True

# if isPresent==True:
#     print("Yes")
# else:
#     print("No")

#################################################################################################################################


# dict2 = {
#     "name":"mahipal",
#     "subjects":["Maths", "English", "Hindi"],
#     "roll_no":2
# }

# output 
# Hi, My name is mahipal.
# My subjects are Maths, English, Hindi.
# My roll_no is 2

# print("Hi, My name is ",dict2["name"], ".")
# print("My subjects are ",dict2["subjects"][0], "," , dict2["subjects"][1], ",", dict2["subjects"][2] , ".")
# print("My roll_no is ", dict2["roll_no"])

##################################################################################################################################

# list1 = ["a", "b", "c", "d"]

# s = "*".join(list1)

# print(s)

# s = "a*b*c*d"

# l = s.split("*")

# print(l)

#################################################################################################################################

2
3
5
8
10
20
44
33
667
77

2
3
5
8
10
20
44
33
667
77

# l = []

# for i in range(0,10):
#     n = int(input("Enter a number: "))

#     l.append(n)

# for i in l:
#     print(i)


# list1 = ["a", "b", "c", "d"]

# output
# ["d", "c", "b", "a"]

###################################################################################################################


# Enter a name: "gaurav"
# Enter a name: "mahipal"
# Enter a name: "komal"
# 10

# "gauarv mahipal komal .............."

# name_list = []

# for i in range(0,10):
#     name = input("Enter a name: ")

#     name_list.append(name)

# # print(name_list)

# print(" ".join(name_list))