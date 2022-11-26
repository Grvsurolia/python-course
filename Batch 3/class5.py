# n = int(input('Enter a Number: '))

# if n%2 == 0:
#     print("Even")
# else:
#     print("odd")

#############################################################################
#### Elif

# if condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# elif condition:
#     statement
# .
# .
# .
# .
# .
# else:
#     statement


n = int(input('Enter a Number: '))

if n < 50:
    print(n," is less then 50")
elif n > 50:
    print(n," is Greater then 50")
else:
    print(n," equal to 50")