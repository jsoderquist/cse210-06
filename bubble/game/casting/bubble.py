import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bubble(Actor):
    """A solid, spherical object that is bounced around in the game."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bubble.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image

    def bounce_x(self):
        """Bounces the bubble in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the bubble in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    #def out_of_bounds(self):
    #    del self

    def get_body(self):
        """Gets the bubble's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the bubble's image.
        
        Returns:
            An instance of Image.
        """

        return self._image
        
    def release(self):
        """Release the bubble in a random direction."""
        rn = random.uniform(0.9, 1.1)
        vx = random.choice([-BUBBLE_VELOCITY * rn, BUBBLE_VELOCITY * rn])
        vy = -BUBBLE_VELOCITY
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)