import turtle
from turtle import Screen, Turtle
import pandas


screen = Screen()
screen.title("US States")
image = "CSVProjects/data/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_states_guessed = 50

while all_states_guessed != 0:
    answer = screen.textinput(title="Guess the state", prompt="Whats the next state?").strip().title()
    data = pandas.read_csv("CSVProjects/data/50_states.csv")
    all_states = data.state.to_list()

    if answer in all_states:
        state_data = data[data.state == answer]
        x = state_data.x.values[0]
        y = state_data.y.values[0]
        tim = Turtle()
        tim.penup()
        tim.goto(x, y)
        tim.write(answer, align="center", font=("Arial", 14, "normal"))
        tim.hideturtle()
        all_states_guessed -= 1
    else:
        print("State not found in dataset.")

screen.exitonclick()