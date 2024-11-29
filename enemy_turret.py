'''
@author: Lucian Kath
@version: 1.0

@datum: 2024-11-26

@description: Basisklasse der im Spiel enthaltenen Gegner
'''
import pygame
import math
import globals
import random
from animated_sprite import SpriteAnimation
from scavengeable import Scavengeable

class EnemyTurret(Scavengeable):
    def __init__(self, screen, maxDurability, resourceDrops):
        super().__init__(screen, maxDurability, resourceDrops)

        rx = random.randint(globals.MAP_X0, globals.MAP_X1)
        ry = random.randint(globals.MAP_Y0, globals.MAP_Y1)

        self.position = [rx, ry]
        self.animation = SpriteAnimation(globals.BASE_PATH + 'assets/sprites/enemy/turret/', 'turret0', 1, '.png')
        self.sprite = self.animation._get_current_sprite()

    def draw(self):        
        offset_x = self.position[0] - globals.camera_offset_x
        offset_y = self.position[1] - globals.camera_offset_y
        self.rect = self.sprite.get_rect(center=(offset_x, offset_y))
        
        self.screen.blit(self.sprite, self.rect)
    
    def defend(self, player):
        sx = self.position[0] - globals.camera_offset_x
        sy = self.position[1] - globals.camera_offset_y
        self_position = pygame.Vector2(sx, sy)
            
        player_position = pygame.Vector2(player.position[0], player.position[1])
            
        distance = self_position.distance_to(player_position)

        rx = sx - player.position[0]
        ry = sy - player.position[1]

        if distance < globals.ENEMY_TURRET_RANGE:
            angle = math.degrees(math.atan2(-ry, rx)) - 90
            self.sprite = pygame.transform.rotate(self.animation._get_current_sprite(), angle)