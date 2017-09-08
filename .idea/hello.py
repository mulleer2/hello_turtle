import turtle

import random

canvas = turtle.Canvas()

gang = []
for x in range(5):
    gang.append(turtle.Turtle())
    gang[x].shape("turtle")

# change all the turtles' color
for x in range(5):
    gang.append(turtle.Turtle())
    gang[x].color("red")

# move all the turtles to a random spot


for x in range(5):
    gang.append(turtle.Turtle())
    gang[x].goto(random.randint(-100, 100),random.randint(-100, 100))
    gang[x].penup()


# EXTRA: make all of the turtles with an even index write a message




input("Press enter to quit")


