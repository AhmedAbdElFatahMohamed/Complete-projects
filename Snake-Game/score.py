from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(x=0,y=270)
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
        self.goto(x=0,y=270)

    def Increase(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=("Arial",20,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",20,"normal"))