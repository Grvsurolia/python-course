# user_input = input("Enter something: ")
# c = input("Enter a char: ")

# if len(user_input) < 10:
#     print("Length of Input should be greater then 10")
#     quit()

# if len(c) != 1:
#     print("Length of C should be 1")
#     quit()

# s = user_input.replace(c, "")

# print(s)

# s = ""


# for i in user_input:
#     if c == i:
#         pass
#     else:
#         s += i

# print(s)

#####################################################################################################

                                                        # *****
                                                        #  ****
                                                        #   ***
                                                        #    **
                                                        #     *

#############################################################################################################################################

#### Classes

## SYNTEX

# class className:
#     statement 


# class First:
#     a = 2
#     b = 3

#     def add(x=a,y=b):
#         return x+y

# print(First.a)

# print(First.b)

# print(First.add(5,6))

# class Second:
#     a = 2

# ob_1 = Second()

# ob_1.b = 3

# print(ob_1.a)

# print(ob_1.b)

# ob_2 = Second()

# ob_2.a = 1

# ob_2.b = 4

# print(ob_2.a)

# print(ob_2.b)


###################################################################

# for i in range(0,5):
#     for j in range(0,i):
#         print("* ",end="")
#     print("# ")

####################################################

# n = 5

# while(n > 0):
#     print(" "*n,end="")
#     n -= 1
#     for i in range(5-n-1):
#         print("* ",end="")
#     print()


###############################################################################################

#### List comprehension

# l = []

# for i in range(0,11):
#     if i % 2 == 0:
#         l.append(i)

# print(l)

# l = [i for i in range(0,11) if i % 2 == 0]
# print(l)

##############################################################################################


even_list = [i if i % 2 == 0 else "gaurav" for i in range(1,11)]
print(even_list)