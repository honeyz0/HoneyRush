#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from codes.Entity import Entity
from codes.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, gameMode):
        self.window = window
        self.name = name
        self.gameMode = gameMode
        self.entityList: list[Entity] = []
        self.entityList.extend(EntityFactory.get_entity('LevelStandard'))

    def run(self, ):
        while True:
            for entity in self.entityList:
                self.window.blit(source=entity.surf, dest=entity.rect)
                entity.move()
            pygame.display.flip()
        pass
