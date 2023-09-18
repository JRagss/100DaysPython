from turtle import Turtle
from constants import THICKNESS, X_POS, Y_POS

class BorderBot:

    def __init__(self):
        super().__init__()
        self.corners = []
        self.make_corners()
        self.go_to_corners()
        self.draw_border()

    def make_corners(self):
        for _ in range(0, 4):
            new_corner = Turtle()
            new_corner.hideturtle()
            new_corner.color('white')
            new_corner.pencolor('white')
            new_corner.pensize(THICKNESS)
            new_corner.penup()
            self.corners.append(new_corner)

    def go_to_corners(self):
        for i in range(0, len(self.corners)):
            self.corners[i].goto(X_POS[i], Y_POS[i])

    def draw_border(self):
        X_POS.append(X_POS[0])
        Y_POS.append(Y_POS[0])
        for i in range(0, len(self.corners)):
            self.corners[i].pendown()
            self.corners[i].goto(X_POS[i+1], Y_POS[i+1])
