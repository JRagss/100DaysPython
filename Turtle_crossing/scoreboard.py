from turtle import Turtle
SCORE_FONT_SIZE = 24
y_location = 300 - 2 * SCORE_FONT_SIZE

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(0, y_location)
        self.pendown()
        self.pencolor('black')
        self.display_score()

    def add_level(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f'Level : {self.score}', move=False, font=('Arial', SCORE_FONT_SIZE, 'normal'), align='center')

    def game_over(self):
        self.home()
        self.write(arg='GAME OVER', move=False, font=('Arial', SCORE_FONT_SIZE, 'normal'), align='center')