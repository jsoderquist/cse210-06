from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
import time


class CollideTankAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        self._delay = 0.3
        self._last = time.time()
        
    def execute(self, cast, script, callback):
        fishes = cast.get_actors(FISH_GROUP)
        tank = cast.get_first_actor(TANK_GROUP)
        
        for fish in fishes:
            fish_body = fish.get_body()
            tank_body = tank.get_body(cast)

            if self._physics_service.has_collided(fish_body, tank_body):
                elapsed = time.time() - self._last

                if elapsed >= self._delay:
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.add_points(FISH_COLLISION)
                    self._last = time.time()