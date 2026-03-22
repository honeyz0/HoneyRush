#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.EntityMediator import EntityMediator
from codes.Const import (COLOR_WHITE, COLOR_YELLOW, WIN_HEIGHT,
                         WIN_WIDTH, MENU_OPTION, EVENT_ENEMY,
                         EVENT_FLOWER, COLOR_RED)
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
        pygame.time.set_timer(EVENT_ENEMY, 2000)
        pygame.time.set_timer(EVENT_FLOWER, 2000)

        self.timeout = 20000
        self.score = 0

    def run(self):
        pygame.mixer_music.load('./assets/Game.wav')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(45)
            for ent in self.entityList:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if ent.name == 'Player':
                    self.level_text(15, f'Health: {ent.health}s', COLOR_WHITE, ((WIN_WIDTH - 895), 28))

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entityList.append(EntityFactory.get_entity('Enemy'))
                if event.type == EVENT_FLOWER:
                    self.entityList.append(EntityFactory.get_entity('FlowerXP'))

                player_alive = any(isinstance(ent, Player) for ent in self.entityList)
                if not player_alive:
                    return self.show_game_over()  # Retorna para o Game decidir o fluxo

            self.level_text(15, f'Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, ((WIN_WIDTH - 880), 15))
            self.level_text(15, f'FPS: {clock.get_fps() :.0f}', COLOR_WHITE, (40, WIN_HEIGHT - 38))
            self.level_text(15, f'Entidades: {len(self.entityList)}', COLOR_WHITE, (60, WIN_HEIGHT - 20))
            self.level_text(20, f'Score: {self.score}', COLOR_YELLOW, (WIN_WIDTH / 2, 50))
            pygame.display.flip()

            EntityMediator.verifyColision(self.entityList, self)
            EntityMediator.verifyHealth(self.entityList)
    pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

    def show_game_over(self):
        pygame.mixer_music.load('./assets/GameOver.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.fill((0, 0, 0))
            self.level_text(70, "GAME OVER", COLOR_RED , (WIN_WIDTH / 2, WIN_HEIGHT / 2 - 100))
            self.level_text(30, f"Final Score: {self.score}", COLOR_WHITE, (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 30))
            self.level_text(20, "Press ENTER to Try Again or ESC for Exit", COLOR_WHITE,
                            (WIN_WIDTH / 2, WIN_HEIGHT / 2 + 90))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: return MENU_OPTION[0]  # Try Again (Play)
                    if event.key == pygame.K_ESCAPE: return "MENU"  # Volta ao menu
                if event.type == pygame.QUIT:
                    pygame.quit();
                    sys.exit()

