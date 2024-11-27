'''
@author: Lucian Kath, Leon Horn
@version: 1.2

@datum: 2024-11-26

@description: Klasse zur Darstellung und dem Umgang mit Planeten und den verschiedenen Typen
'''

import pygame

import globals
from globals import *
from scavengeable import Scavengeable
from animated_sprite import SpriteAnimation

class Planet(Scavengeable):
    def __init__(self, screen, maxDurability, resourceDrops):
        super().__init__(screen, maxDurability, resourceDrops)
        
        self.screen = screen
        self.position = [0, 0]
        self.radius = 48
        
        # self.animation = SpriteAnimation(BASE_PATH, 'Lava', 1, '.png')
        
    def draw(self):
        current_sprite = self.get_current_sprite()
        
        if current_sprite is None:
            return
        
        # Scaling the planet according to the resource drops
        sx = current_sprite.get_width() + 5 * self.resourceDrops
        sy = current_sprite.get_height() + 5 * self.resourceDrops
        scaled_sprite = pygame.transform.scale(current_sprite, (sx, sy))
        self.radius = sx / 2
        
        offset_x = self.position[0] - globals.camera_offset_x
        offset_y = self.position[1] - globals.camera_offset_y
        
        self.screen.blit(scaled_sprite, (offset_x, offset_y))
    
    def get_center_rect(self):
        center_rect = self.animation._get_current_sprite().get_rect(center=(self.position[0], self.position[1]))
        return center_rect
    
    def get_current_sprite(self):
        # self.animation._get_current_sprite()
        if self.animation and self.animation is not None:
            return self.animation._get_current_sprite()

        return self.current_sprite
        
    
    def get_remaining_resources(self):
        return self.resourceDrops
        
    def set_position(self, x, y):
        self.position = [x, y]
        
    def set_remaining_resources(self, amount):
        self.resourceDrops = amount
        
    def set_type(self, planet_type):
        if planet_type in globals.PLANER_TYPES:
            self.animation = SpriteAnimation(BASE_PATH + 'assets/planets/Baren/', 'tile0', 60, '.png')    
        else:
            self.animation = SpriteAnimation(BASE_PATH + 'assets/planets/', planet_type, 1, '.png')