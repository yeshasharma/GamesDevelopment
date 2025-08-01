from turtle import Turtle, Screen
import turtle

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(50)

def move_backward():
    tim.back(50)

def move_count_clock():
    tim.left(25)

def move_clock():
    tim.right(25)

def draw_clear():
    tim.clear()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_count_clock, "a")
screen.onkey(move_clock, "d")
screen.onkey(draw_clear, "c")
screen.listen()
screen.exitonclick()