from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Tank(Actor):
    """A implement used to hit and bounce the bubble in the game."""
    
    def __init__(self, body, animation, debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self, cast):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        stats = cast.get_first_actor(STATS_GROUP)
        self._body.set_size(Point(TANK_INIT_HEIGHT*stats.get_score()*GROWTH_RATE,TANK_INIT_WIDTH*stats.get_score()*GROWTH_RATE))
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def move_left(self):
        """Steers the bat to the left."""
        velocity = Point(-TANK_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def move_right(self):
        """Steers the bat to the right."""
        velocity = Point(TANK_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def move_down(self):
        """Moves the tank down."""
        velocity = Point(0, TANK_VELOCITY)
        self._body.set_velocity(velocity)
        
    def move_up(self):
        """Moves the tank up."""
        velocity = Point(0, -TANK_VELOCITY)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)