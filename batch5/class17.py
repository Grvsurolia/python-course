# d = {
#     "name":"gaurav",
#     "class":2,
#     "age":22
#     }

# p = {}
# for k,v in d.items():
#     p[v] = k 
# print(p)

######################################

# Enter your name: gaurav
# Enter your class  : 2.2
# please enter valid class 
# Enter your class 
# Enter your age
# please enter valid age
# Enter your age

##########################################

name = input("Enter your name: ")
class_ = input("Enter your class: ")

if str(int(float(class_))) != class_:
    print("Please enter valid class")
    class_ = input("Enter your class: ")

age = input("Enter your age: ")
if str(int(float(age))) != age:
    print("Please enter valid age")
    age = input("Enter your age: ")

d = {"name":name, "class":class_, "age":age}
print(d)

