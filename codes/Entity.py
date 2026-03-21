#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.image
from abc import ABC, abstractmethod

# Abstract Class
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets/'+ name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) # Create random
        self.speed = 0

    @abstractmethod # Decorator
    def move(self, ):
        pass
