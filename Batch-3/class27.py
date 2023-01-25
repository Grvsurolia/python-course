## ANY and ALL

# l = [True, True, True, True, True]

# print(any(l))

# print(all(l))

###########################################################

#### WITH STATEMENT

# with open("first.txt", "r") as f:
#     print(f.read())

# f = open("first.txt","r")
# print(f.read())

##########################################################

###### Data compression

# import zlib

# s = b'gaurav dheeraj kamlesh anurag salman kdfh gdshfgdgdgdf bgk dfkgdfhkbgdbgdf bdfk'

# print(len(s))

# t = zlib.compress(s)

# print(t)
# print(len(t))

# import gzip

# data = b'Python - Batteries included'

# with gzip.open("test.txt.gz", "wb") as f:
#     f.write(data)

# import re

# print(dir(re))