import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = Scoreboard()
turtle = Player()
car_manager = CarManager()

screen.listen()

screen.onkeypress(turtle.move_in, 'Up')

num = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()
    if turtle.ycor() > 280:
      turtle.start()
      score.updated_level()
      car_manager.increase_speed()



screen.exitonclick()





