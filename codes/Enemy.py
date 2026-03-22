#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.Const import WIN_WIDTH, ENTITY_SPEED
from codes.Entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]