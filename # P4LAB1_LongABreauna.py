# P4LAB1_LongABreauna
# 04/26/2026
# P4LAB1
# House drawing using turtle graphics Using BOTH a while loop and for a loop

import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("lightblue") # background color

# Create turtle
t = turtle.Turtle()
t.color("brown")
t.pensize(3)


# Move to starting position for
t.penup()
t.goto(-50, 50)
t.pendown()

# DRAW SQUARE (using FOR loop)
for i in range(4):
    t.forward(100)
    t.left(90)

# Move to top of square
t.penup()
t.goto(-50, 150)
t.pendown()

 # Change color of triangle
t.color("green")

# DRAW TRIANGLE (using WHILE loop)
count = 0
while count < 3:
    t.forward(100)
    t.left(120)
    count += 1

# Hide turtle and finish
t.hideturtle()
turtle.done()
