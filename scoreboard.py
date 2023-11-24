from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setposition(-230, 270)
        self.write(f"Level: {self.level}", False, "center", FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "center", FONT)

    def end_game(self):
        self.hideturtle()
        self.penup()
        self.setposition(0, 0)
        self.write("GAME OVER", False, "center", FONT)
