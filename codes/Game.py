#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame

from codes.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from codes.Menu import Menu

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
            menu.run()
            pass



