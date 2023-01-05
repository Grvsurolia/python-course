#### Polymorphism

# s = "djfhghfdh dkjfkjkh"

# print(len(s))

# l = [1,2,3,4,5,6,7,8,8,8,8,8,9,9,9,9,0,0,00]

# print(len(l))

# def add(a,b):
#     print("11111111111111")
#     return a+b

# def add(a,b,c):
#     print("222222222222222")
#     return a+b+c

# print(add(2,3,4))

class First:
    def add(a,b):
        return a+b


class Second:
    def add(a,b):
        return "Hello"+str(a+b)


ob_f = First
# print(ob_f.add(2,3))

ob_s = Second
# print(ob_s.add(2,3))

# for i in (ob_f, ob_s):
#     print(i.add(2,3))

