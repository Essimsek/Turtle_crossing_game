import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280

# Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

# initializing
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        car_manager.increase_speed()
        score_board.level_up()

    car_manager.create_car()
    car_manager.move_cars()

    # detect collision
    if car_manager.detect_collision(player):
        score_board.game_over()
        game_is_on = False

screen.exitonclick()
