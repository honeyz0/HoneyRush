#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.Const import WIN_WIDTH
from codes.Background import Background

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


