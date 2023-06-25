# for i in range(1,11,3):
#     print(i)

# l = [1,2,3,4,5,6,7,8,9,10]

# for i in l:
#     print(i)

###############################

# Enter a number: 2

# even / odd 

# even
# This number is even 
# Table 
# 2 X 1 = 2
# 2 X 2 = 4
# 2 X 3 = 6
# .
# .
# .
# .

# Odd 
# This number is Odd

# n = int(input("Enter a number: "))
# if n%2==0:
#     print("This number is even")
#     for i in range(1,11):
#         print(f"{n} X {i} = {n * i}")
# else:
#     print("This number is odd")

######################################

#### While loop 

# Syntax 

# initialization 
# while Condition:
#     statement 
#     increment / decrement 

# i = 1
# while i<11:
#     print("i = ",i)
#     i = i + 1

# while True:
#     print("Helloooo")

# while True:
#     name = input("Enter a name: ")
#     if name=="gaurav":
#         quit()

#################################

# i = 1
# while i<11:
#     print(2*i)
#     i = i + 1

####################################

# i = 10
# while i>0:
#     print(i)
#     i = i - 1

###################################

# i = 1
# while i<11:
#     print("before = ",i)
#     i = i+1
#     print("after = ",i)
    
############################

# Enter your name: "Gaurav"

# G 
# a 
# u 
# r 
# a 
# v 

# name = input("Enter your name: ")
# # for i in name:
# #     print(i)

# l = len(name)

# i = 0
# while i<l:
#     print(name[i])
#     i = i+1

###########################################

#### Break and continue statements
## Break

# for i in range(1,21):
#     if i==15:
#         break
#     print(i)


# i = 1
# while i<21:
#     if i==15:
#         break
#     print(i)
#     i = i+1

## Continue

# for i in range(1,21):
#     if i==15:
#         continue
#     print(i)