# n = int(input("Enter a number: "))

# def addDigits(n):
#     k = 0
#     while(n > 0):
#         digit = n % 10
#         k += digit
#         n //= 10
#     return k 

# # print(addDigits(n))

# while (n % 10 != n):
#     n = addDigits(n)

# print(n)

###########################################################################################################################

# import re
# xx = "guru99,education is fun 77"
# r1 = re.findall("\d+",xx)
# print(r1)

##########################################################################################################################

# import re
# print((re.split(r'\s','we are splitting the words')))
# print((re.split(r's','split the words')))


#######################################################################################################################

# import re
# xx = """guru99 
# careerguru99	
# selenium"""
# k1 = re.findall(r"^\w", xx)
# k2 = re.findall(r"^\w", xx, re.MULTILINE)
# print(k1)
# print(k2)

###########################################################################################################################


# s = "my name is gaurav"

# print(s)

# print(s.replace("gaurav", "komal"))

#######################################################################################################################

# string = "python is a programming language pagal pagal"

# # replace "p" with "P" once
# print(string.replace("a", "A",3))
 
# # replace "p" with "P" once
# print(string.replace("a", "A")) 

########################################################################################################################

# s = """There are other methods that 55 can be used99 apart from the replace method to replace characters in strings. 754
# However, these methods would involve typecasting or 74 slicing, and concatenation. Although these methods work, 
# they are not preferred over the replace() method. However, I would * recommend you give & them a read and # understand the concept."""

#################################################################################################################

# l = [[1,2,3],[4,5,6]]

# # [[1,4],[2,5],[3,6]]

# a = l[0]
# b = l[1]

# print(list(zip(a,b)))

########################################################################################################################

# import string

# small_alphabet = string.ascii_lowercase

# capital_alphabet = string.ascii_uppercase

# print(list(small_alphabet) + list(capital_alphabet))

##########################################################################################################################

# l = [[1,2,3],[4,5,6]]

# ## [[1,4],[2,5],[3,6]]

# a = l[0]
# b = l[1]

# l2 = list(zip(a,b))
# l3 = []

# for i in l2:
#     l3.append(list(i))

# print(l3)

#############################################################################################################################

import string

small_alphabet_list = list(string.ascii_lowercase)

capital_alphabet_list = list(string.ascii_uppercase)

# print(small_alphabet)
# print(capital_alphabet)
n = input("Enter Something: ")

a = []
b = []

for i in n:
    if i in small_alphabet_list:
        a.append(i)
    elif i in capital_alphabet_list:
        b.append(i)
    else:
        print("Not valid",i)

print(a)
print(b)