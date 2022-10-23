from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Bubble"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "bubble/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "bubble/assets/sounds/boing.wav"
WELCOME_SOUND = "bubble/assets/sounds/start.wav"
OVER_SOUND = "bubble/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)
BLUE = Color(0, 0, 100)

# KEYS
LEFT = "a"
RIGHT = "d"
DOWN = "s"
UP = "w"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"
LEFT_CLICK = "left"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "bubble/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 5
STARTING_POINTS = 8

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "BUBBLE SIZE: {}"

# BUBBLE
BUBBLE_GROUP = "bubbles"
BUBBLE_IMAGE = "bubble/assets/images/000.png"
BUBBLE_WIDTH = 10
BUBBLE_HEIGHT = 10
BUBBLE_VELOCITY = 8

# TANK
TANK_GROUP = "tanks"
TANK_IMAGES = [f"bubble/assets/images/{n:03}.png" for n in range(100, 103)]
TANK_INIT_WIDTH = 30
TANK_INIT_HEIGHT = 30
TANK_RATE = 6
TANK_VELOCITY = 4
GROWTH_RATE = 1/15

# FISH
FISH_GROUP = "fishes"
FISH_IMAGES = [f"bubble/assets/images/{i:03}.png" for i in range(1,2)]
FISH_WIDTH = 50
FISH_HEIGHT = 47
FISH_DELAY = 0.5
FISH_RATE = 4
FISH_POINTS = 3
FISH_VELOCITY = 1
FISH_COLLISION = -7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
WINNER = "YOU SCARED OFF ALL THE FISH AND WON!!"