from turtle import Turtle, Screen
import random


is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter color:")
print(user_bet)
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

turtle_objects = []
for turt in range(len(colors)):
    turtle_objects.append(Turtle(shape="turtle"))

print(turtle_objects)


y_value = -100
i = 0
for turt in turtle_objects:
    turt.color(colors[i])
    turt.penup()
    y_value += 30
    turt.goto(x= -230, y= y_value)
    i += 1


while is_race_on:
    for turt in turtle_objects:
        if turt.xcor() > 220:
            is_race_on = False
            if turt.pencolor() == user_bet:
                print(f"You won!, The color of winning turtle is {turt.pencolor()}")
            else:
                print(f"You lost!, The color of winning turtle is {turt.pencolor()}")
        walk = random.randint(0, 10)
        turt.forward(walk)


# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)
screen.exitonclick()