from turtle import Screen
from border_drawing import BorderBot
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import WIDTH, HEIGHT, play_height, play_width
import time

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
border = BorderBot()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True

LimHeight = play_height / 2 - 20
LimWidth = play_width / 2 - 20
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(.11)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    if (
            snake.head.xcor() > LimWidth or snake.head.xcor() < -LimWidth or
            snake.head.ycor() > LimHeight or snake.head.ycor() < -LimHeight):
        scoreboard.reset()
        snake.reset()

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
