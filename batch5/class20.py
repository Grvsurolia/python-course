# def void_func():
#     pass

# for i in range(30000000):
#     void_func()

#############################################

# import time

# time.sleep(6)

# print("gaurav")

# for i in range(10):
#     time.sleep(1)
#     print("gaurav")

##################################################

# def first(a):

#     def second(b):
#         return str(a)+str(b)

#     return second

# f = first(22)

# print(f(33))


########################################################


# import turtle
# t = turtle.Turtle()

# side = 100

# ## kite boundary
# t.left(45)
# t.forward(side)

# t.right(90)
# t.forward(side)

# t.right(90)
# t.forward(side)

# t.right(90)
# t.forward(side)


# diagonal =  lambda side:(side**2 + side**2)**(1/2)
# ## Horizontal Diagonal
# t.penup()
# t.right(135)
# t.forward(diagonal(side))

# t.pendown()

# t.circle(diagonal(side)/2,180)

# ## vertical Diagonal
# t.penup()
# t.left(135)
# t.forward(100)

# t.pendown()

# t.left(135)
# t.forward(diagonal(side))

# ## Kite Tail
# tail_side = 30
# t.right(45)
# t.forward(tail_side)

# t.left(135)

# t.forward(diagonal(tail_side))

# t.left(135)
# t.forward(tail_side)
# turtle.done()

###########################################

# Python program to draw
# Rainbow Benzene
# using Turtle Programming
# import turtle
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# t = turtle.Pen()
# turtle.bgcolor('black')

# for x in range(360):
#     t.speed(0)
#     t.pencolor(colors[x%6])
#     t.width(x//100)
#     t.forward(x)
#     t.left(90)

# turtle.done()

##########################################

# import turtle 

# t = turtle.Pen()
# t.left(90)
# for x in range(180):
#     t.forward(1)
#     t.right(1)

# turtle.done()


##################################################