import pygame

#C
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 164, 7)
COLOR_GREEN = (0, 255, 0)
COLOR_BLUE = (0, 0, 255)

#E
ENTITY_SPEED = {
    'LevelStandard_0': 0,
    'LevelStandard_1': 2,
    'LevelStandard_2': 1,
    'Player': 5,
    'Enemy': 12,
    'FlowerXP': 8
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_FLOWER = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'LevelStandard_0': 999,
    'LevelStandard_1': 999,
    'LevelStandard_2': 999,
    'Player': 60,
    'Enemy': 60,
    'FlowerXP': 60
}

ENTITY_DAMAGE ={
    'LevelStandard_0': 0,
    'LevelStandard_1': 0,
    'LevelStandard_2': 0,
    'Player': 1,
    'Enemy': 1,
    'FlowerXP': 1
}

ENTITY_SCORE ={
    'LevelStandard_0': 0,
    'LevelStandard_1': 0,
    'LevelStandard_2': 0,
    'Player': 0,
    'Enemy': -10,
    'FlowerXP': 20
}

# M
MENU_OPTION = ('PLAY GAME',
               'TUTORIAL',
               'EXIT')

TUTORIAL_TEXT = ('- Cima',
                 '- Baixo',
                 '- Frente',
                 '- Trás')

# W
WIN_WIDTH = 950
WIN_HEIGHT = 600