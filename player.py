from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.starting_position = STARTING_POSITION
        self.move_distance = MOVE_DISTANCE
        self.setposition(STARTING_POSITION)
        self.color("green")

    def move_up(self):
        self.forward(self.move_distance)

    def reset_turtle(self):
        self.setposition(self.starting_position)
