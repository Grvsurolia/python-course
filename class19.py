# def firstFunc(a="gaurav"):
#     return "hello "+a

# f = firstFunc()
# print(f)

# def a():
#     pass

# for i in range(20000000):
#     a()

# print("hello")

# def a():
#     return "hello"

# print(a())

# del a

# def a():
#     return "Buy Buy"

# print(a())

####################################################
### Closure

# def make_multiplier_of(n):
#     def multiplier(x):
#         print("n = ",n)
#         print("x = ",x)
#         return x * n
#     return multiplier

# times3 = make_multiplier_of(3)

# print(times3(9))

#################################################################################

emp1 = {
    "id":1,
    "name":"gaurav",
    "post":"developer",
    "salary":10,
    "tech": ["python", "c"]
}

emp2 = {
    "id":2,
    "name":"anurag",
    "post":"developer",
    "salary":20,
    "tech": ["python", "c++", "javascript"]
}
# [(1,"gaurav","developer",10,["python","c"]), (2,"anurag","developer",20,["python","c++","javascript"])]

l = []
t = []
for i in emp1:
    t.append(emp1[i])
l.append(tuple(t))

t = []
for i in emp2:
    t.append(emp2[i])
l.append(tuple(t))

print(l)