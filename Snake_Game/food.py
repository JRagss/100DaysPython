from turtle import Turtle
import random

GRID_SIZE = 20
FOOD_LIM = 14


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        randx = random.randint(-FOOD_LIM, FOOD_LIM) * GRID_SIZE
        randy = random.randint(-FOOD_LIM, FOOD_LIM) * GRID_SIZE
        self.goto(randx, randy)
