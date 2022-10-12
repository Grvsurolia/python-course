# n = input("Enter something")

# print(len(n.strip().split()[-1]))

####################################################

# class Calculator:
#     def add(a,b):
#         return a+b
    
#     def sub(a,b):
#         return a-b

# ob1 = Calculator

# ob1.a = 2
# ob1.b = 3

# x = ob1.add(ob1.a, ob1.b)
# y = ob1.sub(2,3)

# print(x,y)

# ob2 = Calculator

# ob2.a = 5
# ob2.b = 6

# x = ob2.add(ob2.a, ob2.b)

# print(x)

####################################################################

# help("modules")

#####################################################################################################################

# n = 1634

# def len_of_n(n):
#     l = 0
#     while(n != 0):
#         n = n//10
#         l += 1
#     return l

# def Armstrong(n):
#     l = len_of_n(n)
#     temp = n
#     sum1 = 0

#     while(temp != 0):
#         r = temp % 10
#         sum1 += r**l
#         print(sum1)
#         temp = temp // 10
#     return (sum1 == n)

# print(Armstrong(n))