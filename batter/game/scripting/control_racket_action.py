from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        if self._keyboard_service.is_key_down(LEFT): 
            racket.move_left()
        elif self._keyboard_service.is_key_down(RIGHT): 
            racket.move_right()
        elif self._keyboard_service.is_key_down(DOWN): 
            racket.move_down()
        elif self._keyboard_service.is_key_down(UP): 
            racket.move_up()
        else: 
            racket.stop_moving()        