'''
@author: Lucian Kath, Leon Horn
@version: 1.2

@datum: 2024-11-26

@description: Klasse zur Darstellung und dem Umgang mit Planeten und den verschiedenen Typen
'''

import pygame
import math

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
        self.scaled_sprite = None
        
    def draw(self):
        scaled_sprite = self.get_scaled_sprite()        
        
        if scaled_sprite is None:
            return
        
        offset_x = self.position[0] - globals.camera_offset_x - self.radius
        offset_y = self.position[1] - globals.camera_offset_y - self.radius
        
        self.screen.blit(scaled_sprite, (offset_x, offset_y))
    
    def get_center(self) -> tuple:
        return self.get_center_rect().center
    
    def get_center_rect(self):
        center_rect = self.get_current_sprite().get_rect()
        return center_rect
    
    def get_current_sprite(self):
        # self.animation._get_current_sprite()
        if self.animation and self.animation is not None:
            return self.animation._get_current_sprite()

        return self.current_sprite
    
    def get_scaled_sprite(self):
        sprite = self.get_current_sprite()
        
        # Scaling the planet according to the resource drops
        sx = sprite.get_width() + 5 * self.resourceDrops
        sy = sprite.get_height() + 5 * self.resourceDrops
        
        self.radius = math.floor(sx / 2)
        self.scaled_sprite = pygame.transform.scale(sprite, (sx, sy))
        
        return self.scaled_sprite
    
    def get_remaining_resources(self):
        return self.resourceDrops
        
    def set_position(self, x, y):
        self.position = [x, y]
        
    def set_remaining_resources(self, amount):
        self.resourceDrops = amount
        
    def set_type(self, planet_type):
        self.animation = SpriteAnimation(BASE_PATH + 'assets/planets/' + planet_type + '/', 'tile0', 60, '.png')    
