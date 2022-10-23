from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideFishAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bubbles = cast.get_actors(BUBBLE_GROUP)
        fishes = cast.get_actors(FISH_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        
        for fish in fishes:
            for bubble in bubbles:
                bubble_body = bubble.get_body()
                fish_body = fish.get_body()

                if self._physics_service.has_collided(bubble_body, fish_body):
                    #bubble.bounce_y()
                    sound = Sound(BOUNCE_SOUND)
                    self._audio_service.play_sound(sound)
                    points = fish.get_points()
                    stats.add_points(points)
                    cast.remove_actor(FISH_GROUP, fish)
                    cast.remove_actor(BUBBLE_GROUP, bubble)