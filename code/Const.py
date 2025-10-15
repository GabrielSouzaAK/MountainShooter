# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 255, 0)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'ShipP1': 3,
    'ShipP2': 3,
    'Enemy1': 2,
    'Enemy2': 1,
}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'QUIT')

# P
PLAYER_KEY_UP = {'ShipP1': pygame.K_UP,
                 'ShipP2': pygame.K_w}
PLAYER_KEY_DOWN = {'ShipP1': pygame.K_DOWN,
                   'ShipP2': pygame.K_s}
PLAYER_KEY_LEFT = {'ShipP1': pygame.K_LEFT,
                   'ShipP2': pygame.K_a}
PLAYER_KEY_RIGHT = {'ShipP1': pygame.K_RIGHT,
                    'ShipP2': pygame.K_d}
PLAYER_KEY_SHOOT = {'ShipP1': pygame.K_RCTRL,
                    'ShipP2': pygame.K_LCTRL}

# S
SPAWN_TIME = 4000

# W
WIN_WIDHT = 576
WIN_HEIGHT = 324
