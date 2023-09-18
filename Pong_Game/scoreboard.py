from turtle import Turtle
from constants import *

score_size = 40
top_home = (HEIGHT/2) - (2*score_size)
player_side = 150
npc_side = -150

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.npc_score = 0
        self.player_score = 0
        self.refresh_scores()

    def refresh_scores(self):
        self.clear()
        self.goto(npc_side, top_home)
        self.write(self.npc_score, align='center', font=("arial", score_size, "normal"))
        self.goto(player_side, top_home)
        self.write(self.player_score, align='center', font=("arial", score_size, "normal"))

    def npc_point(self):
        self.npc_score += 1
        self.refresh_scores()

    def player_point(self):
        self.player_score += 1
        self.refresh_scores()
