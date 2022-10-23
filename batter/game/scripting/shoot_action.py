from constants import *
from game.scripting.action import Action
from game.casting.ball import Ball
from game.casting.body import Body
from game.casting.image import Image
from game.casting.point import Point
from math import sqrt
import time


class ShootAction(Action):

    def __init__(self,mouse_service):
        self._mouse_service = mouse_service
        self._delay = 0.4
        self._last = time.time()

    def execute(self, cast, actor_group, actor):
        elapsed = time.time() - self._last
        stats = cast.get_first_actor(STATS_GROUP)

        if self._mouse_service.is_button_down(LEFT_CLICK) and elapsed >= self._delay:
            self._last = time.time()
            stats.add_points(-1)
            
            tank = cast.get_first_actor(RACKET_GROUP)
            body = tank.get_body(cast)
            tank_position = body.get_position()
            tank_x = tank_position.get_x()
            tank_y = tank_position.get_y()
            tank_size = body.get_size()
            tank_width = tank_size.get_x()
            tank_height = tank_size.get_y()

            mouse = self._mouse_service.get_coordinates()
            mouse_x = mouse.get_x()
            mouse_y = mouse.get_y()

            x = tank_x + tank_width
            y = tank_y + tank_height
            position = Point(x, y)
            size = Point(BALL_WIDTH, BALL_HEIGHT)
            pos_diff_x = mouse_x - tank_x
            pos_diff_y = mouse_y - tank_y
            normalizer = sqrt(pos_diff_x**2 + pos_diff_y**2)
            velocity = Point(pos_diff_x/normalizer*BALL_VELOCITY, pos_diff_y/normalizer*BALL_VELOCITY)
            body = Body(position, size, velocity)
            image = Image(BALL_IMAGE)
            ball = Ball(body, image, True)
            cast.add_actor(BALL_GROUP, ball)


        
        

        