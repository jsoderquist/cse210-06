from constants import *
from game.scripting.action import Action


class MoveBubbleAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        bubbles = cast.get_actors(BUBBLE_GROUP)
        for bubble in bubbles:
            body = bubble.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            body.set_position(position)
