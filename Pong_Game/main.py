from turtle import Screen, Turtle
from constants import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create the screen that the user will play on
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title("PONG")

# setting tracer to 0 turns off animations
screen.tracer(0)

# Creating the score board for the game
scoreboard = Scoreboard()

# creating ball and paddles from their respective classes
ball = Ball()
player_paddle = Paddle('right')
npc_paddle = Paddle('left')

# allows the ability for the user to control their paddle
screen.listen()
screen.onkeypress(player_paddle.go_up, 'Up')
screen.onkeypress(player_paddle.go_down, 'Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.06)
    ball.move()

    # Pass the ball position to the paddle AI to enable the 'impossible' difficulty
    npc_paddle.ball_pos = ball.ycor()
    npc_paddle.paddle_ai('easy')

    # Detect collision with the celling or floor
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce('border')

    # Detect collision with either of the paddles
    elif ball.xcor() >= 330 or ball.xcor() <= -330:
        if ball.distance(player_paddle) < 54 or ball.distance(npc_paddle) < 54:
            ball.bounce('paddle')

    # Detect if the user or npc has scored a point
    if ball.xcor() > 400:
        scoreboard.npc_point()
        ball.reset()

    elif ball.xcor() < -400:
        scoreboard.player_point()
        ball.reset()
screen.exitonclick()
