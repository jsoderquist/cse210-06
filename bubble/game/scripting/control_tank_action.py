from constants import *
from game.scripting.action import Action


class ControlTankAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        tank = cast.get_first_actor(TANK_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            tank.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            tank.move_right()
        elif self._keyboard_service.is_key_down(DOWN): 
            tank.move_down()
        elif self._keyboard_service.is_key_down(UP): 
            tank.move_up()
        else: 
            tank.stop_moving()        