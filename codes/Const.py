import pygame

#C
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 164, 7)

#E
ENTITY_SPEED = {
    'LevelStandard_0': 0,
    'LevelStandard_1': 2,
    'LevelStandard_2': 1,
    'Player': 5,
    'Enemy': 8,
    'FlowerXP': 8
    }

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_FLOWER = pygame.USEREVENT + 1


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