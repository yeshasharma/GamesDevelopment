'''
====== TO DOs ======

Create Screen
Create and move paddle
Create another paddle
Create the ball and make it move
Detect collision with wall and bounce
Detect collision with paddle
Detect when paddle misses
Keep Score
'''

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.listen()

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    ball.move()
    # Detect collision with upper and lower wall
    if ball.ycor() == -280 or ball.ycor() == 280:
        ball.bounce_y()
    
    # Detect collision with the paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
 
    screen.update()

screen.exitonclick()