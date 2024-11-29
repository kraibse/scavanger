'''
@author: Leon Horn
@version: 1.0

@datum: 2024-11-29

@description: Klasse fuer die Darstellung von Projektilen
'''

import pygame

class Projectile:
    def __init__(self):
        self.entity = entity
        self.angle = angle
        self.speed = 10
        self.is_active = False

        self.origin = pygame.Vector2(entity.position[0], entity.position[1])
        self.position = pygame.Vector2(entity.position[0], entity.position[1])

    def shoot_at(self, origin, target_position):
        self.origin = origin
        self.is_active = True
        self.direction = target_position - pygame.Vector2(self.x, self.y)
    
    def draw(self, screen):
        start_pos = self.position - self.direction.scale_to_length(4)
        end_pos = (self.position.x, self.position.y)
        pygame.draw.line(screen, pygame.Color(255, 0, 0), (start_pos.x, start_pos.y), (self.position.x, self.position.y))

    def move(self):
        self.direction = self.direction.scale_to_length(self.speed)
        self.position = pygame.Vector2(self.x + self.direction.x, self.y + self.direction.y)

    def reset(self):
        self.position = self.origin
        self.is_active = False
