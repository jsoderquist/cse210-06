from constants import *
from game.casting.point import Point
from game.scripting.action import Action
from random import randint


class MoveFishAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        fishes = cast.get_actors(BRICK_GROUP)
        for fish in fishes:
            body = fish.get_body()
            position = body.get_position()

            if randint(1,30) == 1:
                body.set_velocity(Point(randint(-20,20)/3,randint(-20,20)/3))

            velocity = body.get_velocity()
            position = position.add(velocity)
            x = position.get_x()
            y = position.get_y()

            if x < 0:
                position = Point(0, position.get_y())
                velocity = Point(randint(0,5), velocity.get_y())
            elif x > (SCREEN_WIDTH - RACKET_INIT_WIDTH):
                position = Point(SCREEN_WIDTH - RACKET_INIT_WIDTH, position.get_y())
                velocity = Point(randint(-5,0), velocity.get_y())
            if y < 0:
                position = Point(position.get_x(),0)
                velocity = Point(velocity.get_x(), randint(0,5))
            elif y > (SCREEN_HEIGHT - RACKET_INIT_HEIGHT):
                position = Point(position.get_x(),SCREEN_HEIGHT - RACKET_INIT_HEIGHT)
                velocity = Point(velocity.get_x(), randint(-5,0))

            body.set_position(position)