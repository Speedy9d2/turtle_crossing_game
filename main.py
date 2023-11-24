import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
the_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    the_count += 1

    car.create_car()
    car.moving_car()

    # Detect if turtle is at the finish line
    if player.ycor() > 280:
        print("You Win!")
        scoreboard.level_up()
        player.reset_turtle()
        car.speed_up()

    # Detect if the turtle collides with car
    for mobiles in car.all_cars:
        if mobiles.distance(player) < 20:
            print("you crashed")
            game_is_on = False
            scoreboard.end_game()


screen.exitonclick()
