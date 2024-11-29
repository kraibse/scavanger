'''
@author: Lucian Kath
@version: 1.0

@datum: 2024-11-26

@description: Basisklasse der im Spiel enthaltenen Gegner
'''
import pygame
import math
import globals
from animated_sprite import SpriteAnimation
from scavengeable import Scavengeable

class EnemyTurret(Scavengeable):
    def __init__(self, screen, maxDurability, resourceDrops):
        super().__init__(screen, maxDurability, resourceDrops)

        self.position = [0, 0]
        self.animation = SpriteAnimation(globals.BASE_PATH + 'assets/sprites/enemy/turret/', 'turret0', 1, '.png')
        self.sprite = self.animation._get_current_sprite()

    def draw(self):        
        offset_x = self.position[0] - globals.camera_offset_x
        offset_y = self.position[1] - globals.camera_offset_y
        self.rect = self.sprite.get_rect(center=(offset_x, offset_y))
        print(self.rect)
        print(self.sprite)
        
        self.screen.blit(self.sprite, self.rect)
    
    def defend(self, player):
        sx = self.position[0] - globals.camera_offset_x
        sy = self.position[1] - globals.camera_offset_y
        self_position = pygame.Vector2(sx, sy)
            
        player_position = pygame.Vector2(player.position[0], player.position[1])
            
        distance = self_position.distance_to(player_position)

        if distance < globals.ENEMY_TURRET_RANGE:
            angle = math.degrees(math.atan2(-sy, sx)) - 90
            self.sprite = pygame.transform.rotate(self.animation._get_current_sprite(), angle)