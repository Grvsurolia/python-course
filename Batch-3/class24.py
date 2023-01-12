# r - read
# w - write
# a - append
# x - create / execute

####### Read

# f = open("first.txt", "r")
# print(f.read())
# print(f.read(20))

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# print(f.readline(5))

# for i in f:
#     print(i)

# f.close()

#### Write

# f = open("first.txt", "a")

# f.write("ggggggggggg aaaaaaaaaaa uuuuuuuuuuuuu rrrrrrrrrrrrr aaaaaaaaaaaa vvvvvvvvvvvvvv")

# f.close()

# f = open("first2.txt", "x")

# import os

# os.remove("first2.txt")

# print(os.path.exists("first2.txt"))

# if os.path.exists("first2.txt")==True:
#     os.remove("first2.txt")
# else:
#     f = open("first2.txt", "x")

# os.rmdir("test_folder")