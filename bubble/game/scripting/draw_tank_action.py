from constants import *
from game.scripting.action import Action


class DrawTankAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        body = tank.get_body(cast)
        stats = cast.get_first_actor(STATS_GROUP)

        if tank.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        animation = tank.get_animation()
        image = animation.next_image()
        image.set_scale(1+stats.get_score()*GROWTH_RATE)
        position = body.get_position()
        self._video_service.draw_image(image, position)