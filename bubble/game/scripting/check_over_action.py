from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        fishes = cast.get_actors(FISH_GROUP)
        if stats.get_score() <= 0 or len(fishes) == 0:
            callback.on_next(GAME_OVER)