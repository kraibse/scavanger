'''
@author: Leon Horn
@version: 1.0

@datum: 2024-11-26

@description: Spielerklasse mit animierten Sprites und der Bewegungsmoeglichkeit
'''

import os
import asyncio
import pygame
import math

from animated_sprite import SpriteAnimation
from globals import SCREEN_W, SCREEN_H

class Player():
    max_speed = 5

    def __init__(self, level):
        w = SCREEN_W
        h = SCREEN_H
        
        self.level = level
        
        self.position = [math.floor(w / 2), math.floor(h / 2)]
        base_path = os.path.dirname(os.path.abspath(__file__)) + '/assets/sprites/player/'
        print(base_path)
        
        self.animations = {
            "idle": SpriteAnimation(base_path, 'player0', 1)
        }

        self.current_animation = "idle"
        # asyncio.run(self.get_current_animation().play())

    def change_animation(self, new_anim="idle"):
        animation = self.get_current_animation()
        asyncio.run(animation.stop())
        
        self.current_animation = new_anim
        asyncio.run(animation.play())
        
    def draw(self):
        current_sprite = self.get_current_animation()._get_current_sprite()
        
        if current_sprite is None:
            return
        
        self.level.screen.blit(current_sprite, (self.position[0], self.position[1]))

    def get_current_animation(self):
        return self.animations.get(self.current_animation)

    def is_accelerating(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        
        return False

    def move(self):
        self.current_animation = "idle"

        mousex, mousey = pygame.mouse.get_pos()
        mx = mousex - self.position[0]
        my = mousey - self.position[1]

        distance = math.sqrt(mx ** 2 + my ** 2)
        if distance == 0:
            return

        # TODO: accelerate and deccelerate smoothly
        motion = [mx / distance * self.max_speed, my / distance * self.max_speed]    # move the player at a constant speed for now

        if self.is_accelerating():
            self.position[0] += motion[0]
            self.position[1] += motion[1]


    def mine(self):
        pass