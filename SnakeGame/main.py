from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.tracer(0)

is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # Detect collisions with the food
    if snake.head.distance(food) < 15:
        snake.create_snake()
        food.refresh()
        scoreboard.score += 1
        scoreboard.show_score()
    
    # Detect collisions with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

screen.exitonclick()