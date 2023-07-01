## File objects and file functions

## Read file content

# f = open("test.txt")
# print(f.read())
# f.close()

#########################

# f = open("test.txt","w")
# f.write("Chandrakanta")
# f.close()

##########################

# Mode of file 

# read = r 
# write = w 
# append = a 

#########################

# f = open("test.txt","a")
# f.write("\nI am a student")
# f.close()

###########################

# import os 
# os.remove("test.txt")

###########################

# Select one option:
# 1. Create a file 
# 2. Write in the file
# 3. Append in the file 
# 4. Delete the file 
# 5. Read the file 

# 1 
# Enter File Name: gaurav.txt 

# 2
# Enter File Name: gaurav.txt 
# Enter your text: I am a developer

# 3
# Enter File Name: gaurav.txt 
# Enter your text: \nI am from jaipur 

# 4
# Enter File Name: gaurav.txt 
# Your file is deleted

# 5
# Enter File Name: gaurav.txt 
# I am a developer
# I am from jaipur 

# n = int(input(""" Select one option:
# 1. Create a file 
# 2. Write in the file
# 3. Append in the file 
# 4. Delete the file 
# 5. Read the file\n"""))

# file_name = input("Enter File Name: ")

# if n==1:
#     f = open(file_name, "w")
#     f.close()
# elif n==2:
#     text = input("Enter your text: ")
#     f = open(file_name,"w")
#     f.write(text)
#     f.close()
# elif n==3:
#     text = input("Enter your text: ")
#     f = open(file_name,"a")
#     f.write(text)
#     f.close()
# elif n==4:
#     import os 
#     os.remove(file_name)
# elif n==5:
#     f = open(file_name,"r")
#     data = f.read()
#     print(data)
#     f.close()
# else:
#     print("Please choose valid option")

##############################################################

# Exception Handling 

## Syntex 

# try:
#     statement 
# except:
#     statement 
# finally:
#     statement 


# Note: 
# Finally is optional 
# except is mandatory with try 

# try:
#     n = int(input("Enter a number: "))

#     print(n)
# except:
#     print("Please enter number")
# finally:
#     print("This program is for finally")
