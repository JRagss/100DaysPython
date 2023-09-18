from turtle import Turtle
import random
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.dist_per_frame = 10
        self.setheading(random.randint(-40, 40))

    def move(self):
        self.forward(self.dist_per_frame)

    def bounce(self, side):
        if side == 'border':
            self.setheading(self.heading() * -1)
        elif side == 'paddle':
            self.setheading(180 - self.heading())
            self.dist_per_frame += 3

    def reset(self):
        self.goto(0, 0)
        self.dist_per_frame = 10
        time.sleep(.25)
        self.bounce('paddle')
