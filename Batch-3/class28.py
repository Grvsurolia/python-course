# l = [1,2,3,4,5,6,7,8,9,10]

# len_l=  len(l)
# p = []

# for i in range(len_l-1,-1,-1):
#     p.append(l[i])

# print(p)

#################################################


# l = [2,3,4,5,6,7,8,9,10,11,12,13]

# len_l=  len(l)

# for i in range(0,len_l//2):
#     print(i, (len_l-1)-i)
#     print("value = ", l[i], l[(len_l-1)-i])
#     l[i], l[(len_l-1)-i] = l[(len_l-1)-i], l[i]

# print(l)

##############################################

# l = [6,5,22,19,1,15,11,1,32,24,3,16]

# m = l[0]

# for i in l:
#     if i > m:
#         m = i
# print(m)

#################################################

# l = [6,5,22,19,1,15,11,1,32,24,3,16]
# count = 0
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         count += 1
#         if l[i]>l[j]:
#             l[i], l[j] = l[j], l[i]
#             print(l)