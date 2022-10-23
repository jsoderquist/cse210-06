from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
import time


class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._delay = 0.3
        self._last = time.time()
        
    def execute(self, cast, script, callback):
        bricks = cast.get_actors(BRICK_GROUP)
        racket = cast.get_first_actor(RACKET_GROUP)
        
        for brick in bricks:
            brick_body = brick.get_body()
            racket_body = racket.get_body(cast)

            if self._physics_service.has_collided(brick_body, racket_body):
                elapsed = time.time() - self._last

                if elapsed >= self._delay:
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.add_points(FISH_COLLISION)
                    self._last = time.time()