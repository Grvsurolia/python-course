# s = {2,3,4,5,6,7}
# l = list(s)
# l[0] = 22
# l[-1] = 77
# print(set(l))


# output:
# {22,3,4,5,6,77}

############################3

# t = (2,3,4,5,6,7)
# l = list(t)
# l[0] = 22
# l[-1] = 77
# print(tuple(l))

# output:
# (22,3,4,5,6,77)

###############################

# l = [2,3,4,5,6]
# print(tuple(l))
# print(set(l))
# print(dict(l))       # Not Possible

# t = (2,3,4,5,6)
# print(list(t))
# print(set(t))
# print(dict(t))      # Not Possible

# s = {2,3,4,5,6}
# print(list(s))
# print(tuple(s))
# print(dict(s))      # Not Possible

# d = {"a":1, "b":2}
# print(list(d))
# print(tuple(d))
# print(set(d))

##############################

# Enter a string: abcde
# Enter second string: edcba

# Write a program to find if First string is reverse of second or not ?
# s1 = input("Enter a string: ")
# s2 = input("Enter second string: ")
# print(f"s1 = {s1}")
# print(f"s2 = {s2}")
# rev_s1 = s1[::-1]
# print(f"rev_s1 = {rev_s1}")
# if rev_s1 == s2:
#     print("Yesssssssssssss")
# else:
#     print("Noooooooooo")
####################################

# l = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# vowel = ["a","e","i","o","u"]
# p = []
# if l[0] in vowel:
#     p.append(l[0])
# if l[1] in vowel:
#     p.append(l[1])
# if l[2] in vowel:
#     p.append(l[2])
# if l[3] in vowel:
#     p.append(l[3])
# if l[4] in vowel:
#     p.append(l[4])
# if l[5] in vowel:
#     p.append(l[5])
# if l[6] in vowel:
#     p.append(l[6])
# if l[7] in vowel:
#     p.append(l[7])
# if l[8] in vowel:
#     p.append(l[8])

# print(p)

# Write a program to extract vowals from the list 

# output:
# ["a", "e", "i"]

####################################

# d = {1:11, 2:22, 3:33}
# l = list(d)
# l2 = [[l[0],d[l[0]]], [l[1],d[l[1]]], [l[2],d[l[2]]]]
# print(l2)
# output:
# [[1,11],[2,22],[3,33]]

############################################

# l = [1,2,3,4]
# s = {1,1,2,2,3,3,4,4}
# print(l,len(l))
# print(s,len(s))

##########################################

# l = [1,2,3,4]
# s = {1,1,2,2,3,3,4,4}
# if len(l)==len(s):
#     print("same")
# else:
#     print("Not same")

##########################################

# Enter your name: anisha

# Your name is Tanisha

#############################################

# d = {
#     "name1":"Anisha",
#     "name2":"Robin",
#     "name3":"Gaurav"
# }

# print(d)
# print(d["name1"])
# print(d.get("name1"))
# d1 = {"name4":"Tanisha"}
# d.update(d1)
# d["name4"] = "Tanisha"
# d.setdefault("name4","Tanisha")
# print(d)

#####################################

# d = {
#     "name1":"Anisha",
#     "name2":"Robin",
#     "name3":"Gaurav"
# }
# d["name2"] = "Robinpreet"
# print(d)
# s_name = input("Enter surname: ")
# d["name1"] = d["name1"] + " " + s_name
# print(d)