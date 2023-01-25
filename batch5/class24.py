#### POLYMORPHISM

# s = "hjsgf bgjdfkgdf  gdfkd jgdf"

# print(len(s))

# l = [2,3,4,5,6,7,8,9,90,0,0,0,0,0,4,4]

# print(len(l))
# print(len(l))
# print(len(l))
# print(len(l))


# def add(x,y,z=0):
#     return x+y+z

# print(add(2,3))
# print(add(2,3,4))
###############################

# class Student:

#     def print_name(self, name):
#         return "hello "+name
    
# class Employee:

#     def print_name(self, name):
#         return "Bye Bye "+name

# s = Student()
# e = Employee()

# print(s.print_name("Dheeraj"))
# print(e.print_name("Kamlesh"))

#######################################

# name = input("Enter name: ")
# try:
#     if name!="gaurav":
#         raise Exception("Enter gaurav")
#     else:
#         print("Hello Gaurav")
# except:
#     print("No Gaurav Found")

#########################################


# def sleep_in(weekday, vacation):
#     if weekday==False or vacation==True:
#         return True
#     else:
#         return False

# print(sleep_in(False, False))
# print(sleep_in(True, False))
# print(sleep_in(False, True))

########################################

# def parrot_trouble(talking, hour):
#     if talking and (hour<7 or hour>20):
#         return True
#     else:
#         return False
    
# print(parrot_trouble(True, 6))
# print(parrot_trouble(False, 7))
# print(parrot_trouble(False, 6))

#############################################

# s= input("enter anything: ")

# def string_splosion(s):
#     a=""
#     for i in range(0,len(s)):
#         print(a)
#         a=a+s[i]
#     # print(a)
        
#     return a
    
# b= string_splosion(s="code")
# print(b)

############################################

# def string_splosion(s):
#     a = ""
#     for i in range(1,len(s)+1):
#         a += s[:i]

#     return a

# print(string_splosion('Code'))
# print(string_splosion('abc'))
# print(string_splosion('ab'))

##########################################