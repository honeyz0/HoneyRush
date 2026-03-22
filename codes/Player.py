#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codes.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from codes.Entity import Entity

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.animationList = []
        for i in range(1):
            img = pygame.image.load(f'./assets/{name}_{i}.png').convert_alpha()
            self.animationList.append(img)

        self.currentFrame = 0
        self.animationSpeed = 1


    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        self.currentFrame += self.animationSpeed
        if self.currentFrame >= len(self.animationList):
            self.currentFrame = 0

        self.surf = self.animationList[int(self.currentFrame)]
        pass
