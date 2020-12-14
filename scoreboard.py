from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-270, 250)
        self.current_level = 1
        self.write(f'Level: {self.current_level}', font=FONT)

    def updated_level(self):
        self.clear()
        self.current_level += 1
        self.write(f'Level: {self.current_level}', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)