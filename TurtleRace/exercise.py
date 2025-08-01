from turtle import Turtle, Screen
import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("blue")
turtle.colormode(255)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# colors = ["red", "green", "blue", "yellow", "pink", "purple",
#           "orange", "black"]
# count = 7
# for i in range(3, 11):
#     for j in range(1, i+1):
#         timmy.forward(100)
#         timmy.right(360/i)
#         timmy.pencolor(colors[count])
#     count -= 1


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

timmy.speed("fastest")

for _ in range(100):
    timmy.color(random_color())
    timmy.circle(180)
    timmy.setheading(timmy.heading() + 10)

screen = Screen()
screen.exitonclick()