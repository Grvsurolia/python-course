#################### Encapsulation

# 1. protected 
# 2. private

# class First:
#     _a = 2  # protected
#     __b = 3 # Private

#     def test1(self):
#         # print("bbbbb",self.__b)
#         return "first function"
    
# class Second(First):
#     b = 3

#     def test2(self):
#         print(self._a)
#         # print("222222222",self.__b)     ## Can not use this private object in another class
#         print(self.b)
#         return "second function"
    
    
    
# fOb = First()
# sOb = Second()

# print(fOb._a)
# print(fOb.test1())
# print(sOb._a)
# print(sOb.test2())