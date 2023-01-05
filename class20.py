
# def string_match(a,b):
#     count = 0
#     for i in range(len(a)-1):
#         if a[i]+a[i+1] in b:
#             count += 1
#     print(count)
        
# string_match('xxcaazz', 'xxbaaz')
# string_match('abc', 'abc')
# string_match('abc', 'axc')

############################

# def array_front9(nums):
#     for i in nums[0:4]:
#         if i == 9:
#             return True
#     return False

# print(array_front9([1, 2, 9, 3, 4]))
# print(array_front9([1, 2, 3, 4, 9]))
# print(array_front9([1, 2, 3, 4, 5]))

########################################

# def make_tags(tag, word):
#     return "<"+tag+">"+word+"</"+tag+">"

# m = make_tags('i', 'Yay')
# print(m)

#########################################

# def make_out_word(out, word):
#     return out[:2] + word + out[2:]

# m = make_out_word('<<>>', 'Yay')
# print(m)

#####################################################################################

## OOPS ( object oriented programming )

## class

# class ClassName:
#     statement 

# a = 2

# def first():
#     print("hello")

#### PEP8

# class FirstClass:
#     a = 3
    
#     def fun():
#         return "I am doing Fun"

# ob1 = FirstClass
# print(ob1.a)

# print(ob1.fun())

##############################

# class Calcy:
#     def add(a, b):
#         return a+b
    
#     def sub(a, b):
#         return a-b
    
#     def multi(a, b):
#         return a*b

# ob1 = Calcy

# print(ob1.add(2,3))
# print(ob1.sub(2,3))

###################################

# class Students:
#     name = ""
#     class_ = 0
#     roll_no = 0

# stu1 = Students
# stu1.name = "Gaurav"
# stu1.class_ = 1
# stu1.roll_no = 10

# print(stu1.name, stu1.class_, stu1.roll_no)

# stu2 = Students
# stu2.name = "Anurag"
# stu2.class_ = 1
# stu2.roll_no = 21

# print(stu2.name, stu2.class_, stu2.roll_no)
