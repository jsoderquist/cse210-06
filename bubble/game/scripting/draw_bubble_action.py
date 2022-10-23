from constants import *
from game.scripting.action import Action


class DrawBubbleAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        bubbles = cast.get_actors(BUBBLE_GROUP)
        for bubble in bubbles:
            body = bubble.get_body()

            if bubble.is_debug():
                rectangle = body.get_rectangle()
                self._video_service.draw_rectangle(rectangle, PURPLE)
                
            image = bubble.get_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)