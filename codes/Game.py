#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame

from codes.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, COLOR_BLUE
from codes.Menu import Menu
from codes.Level import Level

class Game:
    '''
    Class to run the game
    '''
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]: # Menu "PLAY GAME" option
                level = Level(self.window, 'LevelStandard', menu_return)
                level_return = level.run()
                if level_return == 'MENU':
                    break

            elif menu_return == MENU_OPTION[1]: # Menu "OPTIONS" option
                pass

            elif menu_return == MENU_OPTION[2]: # Menu "EXIT" option
                pygame.quit() # Close Window
                sys.exit() # End Pygame
            else:
                pass


