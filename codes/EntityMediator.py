#!/usr/bin/python
# -*- coding: utf-8 -*-
from codes.Entity import Entity
from codes.Enemy import Enemy
from codes.FlowerXP import FlowerXP
from codes.Player import Player


class EntityMediator:

    @staticmethod
    def __verifyColisionWindow(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        pass

    @staticmethod
    def __verifyColisionEntity(ent1, ent2, level_obj):
        if (ent1.rect.colliderect(ent2.rect)):
            # Player collision FlowerXP
            if (isinstance(ent1, Player) and isinstance(ent2, FlowerXP)) or \
                    (isinstance(ent1, FlowerXP) and isinstance(ent2, Player)):
                # Points
                level_obj.score += 25
                if isinstance(ent1, FlowerXP):
                    ent1.health = 0
                else:
                    ent2.health = 0

            # Player collision Enemy
            elif (isinstance(ent1, Player) and isinstance(ent2, Enemy)) or \
                    (isinstance(ent1, Enemy) and isinstance(ent2, Player)):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                level_obj.score = max(0, level_obj.score - 10)

    @staticmethod
    def verifyColision(entityList: list[Entity], level_obj):
        for i in range(len(entityList)):
            entity1 = entityList[i]
            EntityMediator.__verifyColisionWindow(entity1)
            for j in range(i + 1, len(entityList)):
                entity2 = entityList[j]
                EntityMediator.__verifyColisionEntity(entity1, entity2,level_obj)

    @staticmethod
    def verifyHealth(entityList: list[Entity]):
        for ent in entityList:
            if ent.health <= 0:
                entityList.remove(ent)
