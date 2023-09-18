from turtle import Screen
from ball import Ball

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')

ball = Ball()

keep_going = True
while keep_going:
    ball.forward(10)
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce('border')

    # Detect collision with either of the paddles
    elif ball.xcor() >= 290 or ball.xcor() <= -290:
        ball.bounce('paddle')

screen.exitonclick()