from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")

    def write_score(self):
         super().write(f"Score: {self.score}")

    def track(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()
