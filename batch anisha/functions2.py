########## Void/Null function

# def add(a,b):
#     print("a = ",a)
#     print("b = ",b)
#     print("Add = ",a+b)

# add(2,3)

###############################################################

############ Nested function

##### function inside a function 

# def test1(a,b):
#     print("Inside Test 1", a)

#     def test2(b):
#         print("Inside Test 2", b)
#         return b * 10

#     return test2(b)

# c = test1(2,3)
# print(c)

########### return multiple value

# def multiNames():
#     a = input("Enter Name 1: ")
#     b = input("Enter Name 2: ")

#     return a,b

# x,y = multiNames()

# print(x)
# print(y)

##############################################

# a,b,c,d = ['a', 'b', 'c', 'd']
# print("A = ",a)

##############################################

### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# First name: min len = 3, max len = 15, first char should not be numric, required
# Last Name: max len = 15, first char should not be numric, not required
# Email: min len = 5, max len = 25, first char should not be numric, an @ must be there, a . must be there, @ should always come before ., there must be a char before @
# Phone Number: min len 6, max len 10, only numbers, 
# Password: Apply validations by your own
# Confirm password: Apply validations by your own

# Apply all required validations in the above fields

#### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# # Select any one:
# # 1. Area of Circle 
#         Enter radius: 3
#         Area of Circle is: __ 
# # 2. Circumference of circle 
#         Enter radius: 3
#         Circumference of Circle is: __
# # 3. Area of Square
#         ...................
# # 4. Perameter of square
#         ...................
# # 5. Area of Rectangle
#         ...................
# # 6. Perameter of Rectangle
#         ...................

# Create functions for all
### QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ

# l = ['a', 'A', 'b', 'B', 'c', 'C', .............. , 'z', 'Z']

# OUTPUT: {'a':'A', 'b':'B'....................., 'z':'Z'}

# Take the above OUTPUT as INPUT, and reverse the valiues and keys i.e.

# OUTPUT: {'A':'a', 'B':'a'...................,'Z':'z'}