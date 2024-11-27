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

import globals
from globals import SCREEN_W, SCREEN_H, MIN_DISTANCE_TO_CURSOR, MAX_PLAYER_SPEED


class Player():
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
        
        # Calculate the angle to rotate the sprite
        mousex, mousey = pygame.mouse.get_pos()
        mx = mousex - self.position[0]
        my = mousey - self.position[1]
        angle = math.degrees(math.atan2(-my, mx)) - 90  # Negative 'my' because pygame's y-axis is inverted

        rotated_sprite = pygame.transform.rotate(current_sprite, angle)
        sprite_rect = rotated_sprite.get_rect(center=(self.position[0], self.position[1]))
        
        self.level.screen.blit(rotated_sprite, sprite_rect)

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
        if distance <= MIN_DISTANCE_TO_CURSOR:
            return

        motion = [mx / distance * MAX_PLAYER_SPEED, my / distance * MAX_PLAYER_SPEED]    # move the player at a constant speed for now

        if self.is_accelerating():
            # self.position[0] += motion[0]
            # self.position[1] += motion[1]
            globals.camera_offset_x += motion[0]
            globals.camera_offset_y += motion[1]
            
            # print(globals.camera_offset_x, globals.camera_offset_y)


    def mine(self):
        pass