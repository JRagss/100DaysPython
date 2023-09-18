from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)


is_race_on = False
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

x = -220
y = -120

for i in range(0,len(colors)):
    turtles.append(Turtle(shape='turtle'))
    turtles[i].penup()
    turtles[i].color(colors[i])
    y += 40
    turtles[i].goto(x, y)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won, {winning_color} won the race")
            else:
                print(f"You lost, {winning_color} won the race")
        random_step = random.randint(0, 10)
        turtle.forward(random_step)









screen.exitonclick()
