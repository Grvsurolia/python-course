##### Exceptional Handling (Error Handling)

## Syntex
# try:
#     statement
# except:
#     statement
# finally:
#     statement

# try:
#     for i in range(20):
#         if i==7:
#             prin(i)
#         print(i)

# except:
#     print("Error")

###################

# try:
#     print(3/0)
# except:
#     print("can not divide by zero")

###################
# try:
#     n = int(input("Enter an value: "))

#     for i in range(1,10):
#         print(n*i)
# except Exception as e:
#     print("Please enter valid input")
# finally:
#     try:
#         n = int(input("Enter an value: "))

#         for i in range(1,10):
#             print(n*i)
#     except:
#         print("Please enter valid input")

########################


# try:
#     n = int(input("Enter an value: "))

#     for i in range(1,10):
#         print(n*i)
# except Exception as e:
#     print("Please enter valid input",e)