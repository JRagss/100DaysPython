from turtle import Turtle
from constants import *


STEP_SIZE = 15

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.color('white')
        self.shape('square')
        self.penup()
        self.speed('fastest')
        self.paddles_go_to_positions()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.ball_pos = 0
        self.can_move_up = True

    def paddles_go_to_positions(self):
        if self.side == 'right':
            self.goto(right_start)

        if self.side == 'left':
            self.goto(left_start)

    def go_up(self):
        if self.ycor() >= 240:
            self.can_move_up = False
            pass
        else:
            x = self.xcor()
            y = self.ycor()
            self.setpos(x, y + STEP_SIZE)

    def go_down(self):
        if self.ycor() <= -230:
            self.can_move_up = True
            pass
        else:
            x = self.xcor()
            y = self.ycor()
            self.setpos(x, y - STEP_SIZE)

    def paddle_ai(self, difficulty):
        if difficulty == 'easy':
            if self.can_move_up:
                self.go_up()
            else:
                self.go_down()

        elif difficulty == 'impossible':
            x = self.xcor()
            y = self.ball_pos
            self.goto(x, y)
