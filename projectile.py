'''
@author: Leon Horn
@version: 1.0

@datum: 2024-11-29

@description: Klasse fuer die Darstellung von Projektilen
'''

import pygame

class Projectile:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10

    def shoot_at(self, target_position):
        self.direction = target_position - pygame.Vector2(self.x, self.y)
    
    def move(self):
        self.direction = self.direction.scale_to_length(self.speed)
        self.position = pygame.Vector2(self.x + self.direction.x, self.y + self.direction.y)