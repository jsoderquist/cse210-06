from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        bubbles = cast.get_actors(BUBBLE_GROUP)
        for bubble in bubbles:
            body = bubble.get_body()
            position = body.get_position()
            x = position.get_x()
            y = position.get_y()
            bounce_sound = Sound(BOUNCE_SOUND)
            over_sound = Sound(OVER_SOUND)
                    
            if x < FIELD_LEFT or x >= (FIELD_RIGHT) or y < 0 or y >= (FIELD_BOTTOM):
                cast.remove_actor(BUBBLE_GROUP, bubble)

        """
        elif y >= (FIELD_BOTTOM - BUBBLE_WIDTH):
            stats = cast.get_first_actor(STATS_GROUP)
            stats.lose_life()
            
            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)
        """