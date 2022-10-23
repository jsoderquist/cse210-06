from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.point import Point
from game.scripting.action import Action
from random import randint


class AddFishAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        if randint(1,100) == 1:
            x = randint(0,SCREEN_WIDTH)
            y = randint(0,SCREEN_HEIGHT)
            points = BRICK_POINTS 
            
            position = Point(x, y)
            size = Point(BRICK_WIDTH, BRICK_HEIGHT)
            velocity = Point(FISH_VELOCITY, FISH_VELOCITY)
            images = BRICK_IMAGES

            body = Body(position, size, velocity)
            animation = Animation(images, BRICK_RATE, BRICK_DELAY)

            brick = Brick(body, animation, points, size)
            cast.add_actor(BRICK_GROUP, brick)