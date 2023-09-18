from turtle import Turtle
from constants import Y_Location, SCORE_FONT_SIZE, GAME_OVER_FONT_SIZE


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, Y_Location)
        self.pencolor('white')
        with open("data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.display_score()

    def add_point(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f'Score : {self.score} | High Score : {self.high_score}', move=False, font=('Arial', SCORE_FONT_SIZE, 'normal'), align='center')

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.score}")
        self.score = 0
        self.display_score()


