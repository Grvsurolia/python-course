# def table(n):
#     for i in range(1,11):
#         print(n * i)

# a = int(input("Enter a number: "))
# table(a)


###############################################################################################

# def table(n):
#     for i in range(1,11):
#         if i%2 != 0:
#             print(n * i)

# a = int(input("Enter a number: "))
# table(a)

#################################################################################################

# name = input("Enter Your Name: ")
# class_ = int(input("Enter Your Class: "))
# roll_no = int(input("Enter Your Roll No: "))
# city = input("Enter Your city: ")
# country = input("Enter Your country: ")

# key = []
# values = []

# key.append("name")
# key.append("class_")
# key.append("roll_no")
# key.append("city")
# key.append("country")

# values.append(name)
# values.append(class_)
# values.append(roll_no)
# values.append(city)
# values.append(country)

# print(key)
# print(values)











# Output

# ["name", "class", "roll_no", "city", "country"]
# ["Gaurav", "2", "7", "Jaipur", "India"]



# keys = ["name", "class", "roll_no", "city", "country"]
# values = ["Gaurav", "2", "7", "Jaipur", "India"]

# print(dict(zip(keys, values)))
# print(list(zip(keys, values)))
# print(tuple(zip(keys, values)))
# print(set(zip(keys, values)))

#########################################################################################################################

# i = 10

# n = int(input('Enter a number: '))

# while(i >= 1):

#     print(n * i)

#     i -= 1

###########################################################################################################################

# l = ["a", "b", "c", "d", "e", "f", "g"]

# s = ""

# for i in l:
#     s = s + i

# print(s)

# print("".join(l))

######################################################################################################################

# l = [["a", "b"], ["c", "d"], ["e", "f"]]

# for i in l:
#     print("i = ",i)
#     for j in i:
#         print("j = ",j)

#######################################################################################################################

def multipy(a, *args, ):
    print(a,args)
    for i in args:
        print(i)

multipy("a", "b", "c")