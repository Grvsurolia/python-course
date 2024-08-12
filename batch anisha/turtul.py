import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Little Turtle")
turt = turtle.Turtle()

# turt.forward(100)
# turt.right(90)
# turt.forward(200)
# turt.right(90)
# turt.forward(100)
# turt.right(90)
# turt.forward(200)

# for i in range(5):
#     turt.forward(100)
#     turt.right(145)

# turtle.done()

######################################

# import turtle 

# # Set up the turtle screen and set the background color to white 
# screen = turtle.Screen() 
# screen.bgcolor("white") 

# # Create a new turtle and set its speed to the fastest possible 
# pen = turtle.Turtle() 
# pen.speed(3) 

# # Set the fill color to red 
# pen.fillcolor("red") 
# pen.begin_fill() 

# # Draw the circle with a radius of 100 pixels 
# pen.circle(100)

# # End the fill and stop drawing 
# pen.end_fill() 
# pen.hideturtle() 

# # Keep the turtle window open until it is manually closed 
# turtle.done() 


# # import package 
# import turtle  
  
# # loop for pattern 
# for i in range(20): 
    
#   # set turtle speed 
#   turtle.speed(10-i) 
    
#   # motion for pattern 
#   turtle.forward(50+10*i) 
#   turtle.right(90)


# Python program to draw  
# Spiral  Helix Pattern 
# using Turtle Programming 
  
# import turtle 
# loadWindow = turtle.Screen() 
# turtle.speed(0) 
  
# for i in range(100): 
#     turtle.circle(5*i) 
#     turtle.circle(-5*i) 
#     turtle.left(i) 
  
# turtle.exitonclick() 


# Python program to draw 
# Rainbow Benzene 
# # using Turtle Programming 
# import turtle 
# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
# t = turtle.Pen() 
# turtle.bgcolor('black') 
# for x in range(360): 
# 	t.pencolor(colors[x%6]) 
# 	t.width(x//100 + 1) 
# 	t.forward(x) 
# 	t.left(59) 
