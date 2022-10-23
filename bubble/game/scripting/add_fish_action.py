from constants import *
from game.casting.animation import Animation
from game.casting.body import Body
from game.casting.fish import Fish
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
            points = FISH_POINTS 
            
            position = Point(x, y)
            size = Point(FISH_WIDTH, FISH_HEIGHT)
            velocity = Point(FISH_VELOCITY, FISH_VELOCITY)
            images = FISH_IMAGES

            body = Body(position, size, velocity)
            animation = Animation(images, FISH_RATE, FISH_DELAY)

            fish = Fish(body, animation, points, size)
            cast.add_actor(FISH_GROUP, fish)