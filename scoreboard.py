from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.draw_roads()
        self.level = 1
        self.pen = Turtle()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(-200, 260)
        self.pen.write(arg=f"Level: {self.level}", font=FONT)



    @staticmethod
    def draw_roads():
        pen = Turtle()
        pen.hideturtle()
        y = -250
        while y < 250:
            x = 280
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            while x > -280:
                pen.backward(20)
                pen.penup()
                pen.backward(20)
                pen.pendown()
                x -= 20
            y += 40

    def level_up(self):
        self.level += 1
        self.pen.clear()
        self.pen.write(arg=f"Level: {self.level}", font=FONT)

    @staticmethod
    def game_over():
        last_word = Turtle()
        last_word.penup()
        last_word.goto(0, 0)
        last_word.write(arg="Game over",align="center", font=FONT)

