import random
from turtle import Turtle
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_START_POS = 300

class CarManager:
    def __init__(self):
        self.cars: list[Turtle] = []
        self.speed = STARTING_MOVE_DISTANCE
        self.create_car()
        self.count = 0

    def create_car(self):
        if random.randint(0, 6) == 1:
            new_car = Turtle(shape="square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_pos = random.randint(-250, 250)
            x_pos = CAR_START_POS
            new_car.goto(x_pos, y_pos)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)
            # delete the car if out of screen
            if car.xcor() <= -300:
                index = self.cars.index(car)
                car.clear()
                car.hideturtle()
                del car
                self.cars.pop(index)

    def detect_collision(self, player: Player) -> bool:
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False


    def increase_speed(self):
        self.speed += MOVE_INCREMENT
