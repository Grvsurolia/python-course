# d = {
#     "name":"Gaurav",
#     "age":2,
#     "class":3,
#     "course":"Python"
# }

# for i in d:
    # print("Your",i,"is", d[i], end=", ")
    # print(f"Your {i} is {d[i]}", end=", ")


# output: "Your name is Gaurav, Your age is 2, Your class is 3, Your course is python"
##############################################

# Enter Your Name: Gaurav
# Enter Your Age: 22
# Enter Your Class: 7
# Enter Your Course: Python

# l = ["name", "age", "class", "course"]
# d = {}
# for i in l:
#     n = input(f"Enter Your {i}: ")
#     d[i] = n

# print(d)


# Output: 
# {
#     "name":"Gaurav",
#     "age":22,
#     "class":7,
#     "course":"Python"
# }

###########################################

# t = ("abhishek", "ankit", "aman", "arpit", "divyansh")
# l = list(t)
# p = []
# count = 1
# for i in l:
#     p.append(i+str(count))
#     count = count + 1
# print(tuple(p))

# output: 
# ("abhishek1", "ankit2", "aman3", "arpit4", "divyansh5")

###############################################

## While Loop syntax

# initialize
# while condition:
#     statement
#     increment / decrement

# i = 1
# while i<=10:
#     print("i = ",i)
#     i += 1

#####################

# i = 2
# while i<=20:
#     print(i)
#     i += 2

# i = 1
# while i<=10:
#     print(2*i)
#     i += 1

###############################

# i = 20
# while i>=1:
#     print(i)
#     i -= 1

################################################

# while True:
#     print("Hellooo")

##############################################

# l = ["a","e","i","o","u"]
# name = input("Enter your name: ")
# count = 0
# for i in name:
#     if i in l:
#         count += 1

# print(count)

##########################################
## Break statement

# for i in range(0,20):
#     if i==11:
#         break
#     print(i)

## Continue statement

# for i in range(0,20):
#     if i==11:
#         continue
#     print(i)