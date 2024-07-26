# # 1. create
# # open("test1.txt",'w')

# # 1.1 open 
# f = open("test1.txt","w+")
# print(f)

# # 2. read 
# # print(f.read())
# # print(f.readline())
# # print(f.readline())
# # print(f.readlines())

# # 3. write 
# f.write("gggggggggggggggggggggggggggggggggggggg")
# print("111111 =",f.read())
# # 4. append 
# # f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")

# # 5. close 
# # f.close()

# # print(f.name)
# print(f.closed)
# # print(f.buffer)
# # print(f.mode)

# f.flush()
# print("22222 =",f.read())
# print(f.closed)

# f.write("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
# print("333333 =",f.read())

# f.close()

# f = open('test3.txt', 'a+')
# f.seek(0)
# print(f.read())
# f.write("4444444444444")
# f.seek(0)
# print(f.read())
# f = open('test3.txt','r')
# print(f.read())

# with open('test1.txt','w+') as f:
#     f.write("bbbbbbbbbbbb")
#     f.seek(0)
#     print(f.read())


# Delete a file 

# import os 

# # os.remove('test3.txt')
# current_path = os.getcwd()

# # print(current_path.split("\\")[-1])

# file_name = "test2.txt"

# # path = current_path + "\\" +file_name

# new_dir = 'test_dir'
# os.mkdir(new_dir)

# path = os.path.join(current_path, new_dir, file_name)
# print(path)

# ## To create new file
# open(path, 'w')

######## QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ


# Select one from below:
# 1. Create new file 
# 2. edit a file 
# 3. delete a file 
# 4. read a file 

# 1
# Enter file name/path : 'test2.txt'
# Your file with name test2.txt is created

# Select one from below:
# 1. Create new file 
# 2. edit a file 
# 3. delete a file 

# 2
# Enter file name/path : 'test2.txt'

# Select one from below:
# 1. overwrite the file 
# 2. append in the file 

# 1
# write something: kjsghfb shfdbhfsd vjhdfsvhj db vhjdshjbfd hjb

# 2
# write something: kjsghfb shfdbhfsd vjhdfsvhj db vhjdshjbfd hjb

# Select one from below:
# 1. Create new file 
# 2. edit a file 
# 3. delete a file 

# 3
# Enter file name/path : 'test2.txt'

# your file with name tst2.txt is deleted

# 4
# File content:
# File content HERE