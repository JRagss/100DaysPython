import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)

# disabling animations within the screen
screen.tracer(0)

# Creating the scoreboard object
scoreboard = Scoreboard()

# Creating the player and the car making system
player = Player()
car = CarManager()

# enabling the user to control the player turtle
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Attempt to spawn a new car
    car.attempt_spawn()
    car.move()

    # Remove cars that have exited the left side of the screen
    if car.cars:
        car.check_expired()

    # Check if the player has been hit by a car
    for each_car in car.cars:
        if each_car.ycor() >= player.ycor() and player.distance(each_car) <= 25:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() >= 270:
        player.goto(0, -280)
        scoreboard.add_level()
        print(scoreboard.score)
        car.increase_speed()

screen.exitonclick()
