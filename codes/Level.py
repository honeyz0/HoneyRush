#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface,Rect
from pygame.font import Font

from codes.Const import COLOR_WHITE, WIN_HEIGHT, WIN_WIDTH, MENU_OPTION, EVENT_ENEMY, EVENT_FLOWER
from codes.Entity import Entity
from codes.EntityFactory import EntityFactory
from codes.Player import Player


class Level:
    def __init__(self, window, name, gameMode):
        self.window = window
        self.name = name
        self.gameMode = gameMode
        self.entityList: list[Entity] = []

        self.entityList.extend(EntityFactory.get_entity('LevelStandard'))
        self.entityList.append(EntityFactory.get_entity('Player'))
        self.entityList.append(EntityFactory.get_entity('FlowerXP'))
        self.entityList.append(EntityFactory.get_entity('Enemy'))
        if gameMode in [MENU_OPTION[1]]:
            self.entityList.append(EntityFactory.get_entity('Player'))
        if gameMode in [MENU_OPTION[1]]:
            self.entityList.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)
        pygame.time.set_timer(EVENT_FLOWER, 4000)

        self.timeout = 20000


    def run(self):
        pygame.mixer_music.load('./assets/Game.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(45)
            for entity in self.entityList:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entityList.append(EntityFactory.get_entity('Enemy'))
                if event.type == EVENT_FLOWER:
                    self.entityList.append(EntityFactory.get_entity('FlowerXP'))

            self.level_text(15, f'Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, ((WIN_WIDTH - 880), 15))
            self.level_text(15, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (40, WIN_HEIGHT - 38))
            self.level_text(15, f'Entidades: {len(self.entityList)}', COLOR_WHITE, (60, WIN_HEIGHT - 20))
            pygame.display.flip()
    pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)