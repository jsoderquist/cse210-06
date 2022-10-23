import csv
from os import statvfs_result
from constants import *
from game.casting.animation import Animation
from game.casting.bubble import Bubble
from game.casting.body import Body
from game.casting.fish import Fish
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.tank import Tank
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.add_fish_action import AddFishAction
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_fish_action import CollideFishAction
from game.scripting.collide_tank_action import CollideTankAction
from game.scripting.control_tank_action import ControlTankAction
from game.scripting.draw_bubble_action import DrawBubbleAction
from game.scripting.draw_fishes_action import DrawFishesAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_tank_action import DrawTankAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.services.raylib.raylib_mouse_service import RaylibMouseService
from game.scripting.move_bubble_action import MoveBubbleAction
from game.scripting.move_fish_action import MoveFishAction
from game.scripting.move_tank_action import MoveTankAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.shoot_action import ShootAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService
from random import randint


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    MOUSE_SERVICE = RaylibMouseService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    ADD_FISH_ACTION = AddFishAction()
    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_FISHES_ACTION = CollideFishAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_TANK_ACTION = CollideTankAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_TANK_ACTION = ControlTankAction(KEYBOARD_SERVICE)
    DRAW_BUBBLE_ACTION = DrawBubbleAction(VIDEO_SERVICE)
    DRAW_FISHES_ACTION = DrawFishesAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_TANK_ACTION= DrawTankAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BUBBLE_ACTION = MoveBubbleAction()
    MOVE_FISH_ACTION = MoveFishAction()
    MOVE_TANK_ACTION = MoveTankAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    SHOOT_ACTION = ShootAction(MOUSE_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        #self._add_level(cast)
        #self._add_lives(cast)
        self._add_score(cast)
        stats = cast.get_first_actor(STATS_GROUP)
        stats.add_points(STARTING_POINTS)
        #self._add_bubble(cast)
        cast.clear_actors(FISH_GROUP)
        for i in range(5):
            self._add_fishes(cast)
        self._add_tank(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        #self._add_bubble(cast)
        self._add_fishes(cast)
        self._add_tank(cast)
        #self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 0))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        #self._add_bubble(cast)
        self._add_tank(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 0))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        #self._activate_bubble(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_TANK_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        #self._add_bubble(cast)
        stats = cast.get_first_actor(STATS_GROUP)

        self._add_tank(cast)
        if stats.get_score() <= 0:
            self._add_dialog(cast, WAS_GOOD_GAME)
        else:
            self._add_dialog(cast, WINNER)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_bubble(self, cast):
        bubble = cast.get_first_actor(BUBBLE_GROUP)
        bubble.release()

    def _add_bubble(self, cast):
        cast.clear_actors(BUBBLE_GROUP)
        x = CENTER_X - BUBBLE_WIDTH / 2
        y = SCREEN_HEIGHT - TANK_INIT_HEIGHT - BUBBLE_HEIGHT  
        position = Point(x, y)
        size = Point(BUBBLE_WIDTH, BUBBLE_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BUBBLE_IMAGE)
        bubble = Bubble(body, image, True)
        cast.add_actor(BUBBLE_GROUP, bubble)

    def _add_fishes(self, cast):
        x = randint(0,SCREEN_WIDTH)
        y = randint(0,SCREEN_HEIGHT)
        points = FISH_POINTS 
        
        position = Point(x, y)
        size = Point(FISH_WIDTH, FISH_HEIGHT)
        velocity = Point(FISH_VELOCITY, FISH_VELOCITY)
        images = FISH_IMAGES

        body = Body(position, size, velocity)
        animation = Animation(images, FISH_RATE, FISH_DELAY)

        fish = Fish(body, animation, points, size)
        cast.add_actor(FISH_GROUP, fish)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    """
    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)
    

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)
    """

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_tank(self, cast):
        cast.clear_actors(TANK_GROUP)
        x = CENTER_X - TANK_INIT_WIDTH / 2
        y = SCREEN_HEIGHT - TANK_INIT_HEIGHT
        position = Point(x, y)
        size = Point(TANK_INIT_WIDTH, TANK_INIT_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(TANK_IMAGES, TANK_RATE)
        tank = Tank(body, animation)
        cast.add_actor(TANK_GROUP, tank)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BUBBLE_ACTION)
        script.add_action(OUTPUT, self.DRAW_FISHES_ACTION)
        script.add_action(OUTPUT, self.DRAW_TANK_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BUBBLE_ACTION)
        script.add_action(UPDATE, self.MOVE_TANK_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_FISHES_ACTION)
        script.add_action(UPDATE, self.COLLIDE_TANK_ACTION)
        script.add_action(UPDATE, self.MOVE_TANK_ACTION)
        script.add_action(UPDATE, self.MOVE_FISH_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
        script.add_action(UPDATE, self.SHOOT_ACTION)
        script.add_action(UPDATE, self.ADD_FISH_ACTION)