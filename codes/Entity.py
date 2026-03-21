#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from abc import ABC, abstractmethod
from codes.Const import WIN_WIDTH, WIN_HEIGHT

# Abstract Class
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/'+ name + '.png').convert_alpha()
        #self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # Create random
        self.speed = 0

    @abstractmethod # Decorator
    def move(self, ):
        pass
