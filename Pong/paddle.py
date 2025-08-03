from turtle import Turtle
LEFT_CORD = -350
RIGHT_CORD = 350

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(pos)
    
    def move_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def move_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
