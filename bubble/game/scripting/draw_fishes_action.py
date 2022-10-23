from constants import *
from game.scripting.action import Action


class DrawFishesAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        fishes = cast.get_actors(FISH_GROUP)
        
        for fish in fishes:
            body = fish.get_body()

            if fish.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            animation = fish.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)