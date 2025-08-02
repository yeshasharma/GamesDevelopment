from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_DISTANCE = 90
LEFT_DISTANCE = 180
DOWN_DISTANCE = 270
RIGHT_DISTANCE = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            t = Turtle("square")
            t.penup()
            t.color("white")
            t.goto(position)
            self.segments.append(t)
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            xcor = self.segments[seg_num-1].xcor()
            ycor = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(xcor, ycor)
        self.head.forward(MOVE_DISTANCE)
        # segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN_DISTANCE:
            self.head.setheading(UP_DISTANCE)
    
    def left(self):
        if self.head.heading() != RIGHT_DISTANCE:
            self.head.setheading(LEFT_DISTANCE)
    
    def down(self):
        if self.head.heading() != UP_DISTANCE:
            self.head.setheading(DOWN_DISTANCE)
    
    def right(self):
        if self.head.heading() != LEFT_DISTANCE:
            self.head.setheading(RIGHT_DISTANCE)

    