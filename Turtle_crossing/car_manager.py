from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_LENGTH_FACTOR = 2.25
STARTING_X = 300 + round((20 * CAR_LENGTH_FACTOR) / 2)
SCREEN_INDEX_MAX = int(300 / 20) - 1


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        super().ht()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def attempt_spawn(self):
        attempt_int = random.randint(0, 100)
        if attempt_int > 86:
            self.spawn_car()
        else:
            pass

    def spawn_car(self):
        new_car = Turtle('square')
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=CAR_LENGTH_FACTOR)
        new_car.penup()
        new_car.setheading(180)
        starting_y = 20 * random.randint(-SCREEN_INDEX_MAX + 1, SCREEN_INDEX_MAX)
        new_car.goto(STARTING_X, starting_y)
        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def check_expired(self):
        if self.cars[0].xcor() < -STARTING_X:
            del self.cars[0]

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
