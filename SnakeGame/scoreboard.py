from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.show_score()

    
    def show_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=('Arial', 24, 'normal'))
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 24, 'normal'))