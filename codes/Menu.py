#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codes.Const import WIN_WIDTH, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW

class Menu:
    '''
    Class to create and run the menu screen
    '''
    def __init__(self, window):
        self.window = window

        originalLogo = pygame.image.load('./assets/GameLogo.png')
        self.surf = pygame.image.load('./assets/GameBackground.jpg')

        self.logo = pygame.transform.smoothscale_by(originalLogo, 0.3)

        self.rect = self.surf.get_rect(left=0, top=0)
        self.logo_rect = self.logo.get_rect(center=(WIN_WIDTH / 2, 220))


    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/Menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.window.blit(source=self.logo, dest=self.logo_rect)
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(55, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH/2), 500 + 80 * i))
                else:
                    self.menu_text(55, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 500 + 80 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit()  # End Pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


    #def tutorial(self, ):
    #    pass

    #def exit(self, ):
    #    pass
