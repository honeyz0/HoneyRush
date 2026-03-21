#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from codes.Const import WIN_WIDTH, WIN_HEIGHT
from codes.Background import Background
from codes.Enemy import Enemy
from codes.Player import Player
from codes.FlowerXP import FlowerXP


class EntityFactory:
    '''
    Create random entitys
    '''

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'LevelStandard':
                list_LevelStandard = []
                for i in range(3):
                    list_LevelStandard.append(Background(f'LevelStandard_{i}', (0, 0)))
                    list_LevelStandard.append(Background(f'LevelStandard_{i}', (WIN_WIDTH, 0)))
                return list_LevelStandard
            case 'Player':
                return Player('Player', (10, (WIN_HEIGHT / 2)))
            case 'FlowerXP':
                return FlowerXP('FlowerXP', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Enemy':
                return Enemy('Enemy', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))