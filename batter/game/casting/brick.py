from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Brick(Actor):
    """A solid, rectangular object that can be broken."""

    def __init__(self, body, animation, points, size, debug = False):
        """Constructs a new Brick.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        self._size = size
        
    def get_animation(self):
        """Gets the brick's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the brick's body.
        
        Returns:
            An instance of Body.
        """
        #self._body.set_size(Point(BRICK_HEIGHT*self._size.get_x(), BRICK_WIDTH*self._size.get_y()))

        return self._body

    def get_points(self):
        """Gets the brick's points.
        
        Returns:
            A number representing the brick's points.
        """
        return self._points