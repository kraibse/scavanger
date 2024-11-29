'''
@author: Lucian Kath
@version: 1.0

@datum: 2024-11-26

@description: Basisklasse der im Spiel enthaltenen Gegner
'''
import pygame
import math
import globals

from projectile import Projectile
from animated_sprite import SpriteAnimation
from scavengeable import Scavengeable

class EnemyTurret(Scavengeable):
    def __init__(self, screen, maxDurability, resourceDrops):
        super().__init__(screen, maxDurability, resourceDrops)

        self.position = [0, 0]
        self.projectiles = [
            # Projectile(self),
            # Projectile(self),
            # Projectile(self),
            # Projectile(self),
            # Projectile(self)
        ]

        self.animation = SpriteAnimation(globals.BASE_PATH + 'assets/sprites/enemy/turret/', 'turret0', 1, '.png')
        self.sprite = self.animation._get_current_sprite()

    def draw(self):        
        offset_x = self.position[0] - globals.camera_offset_x
        offset_y = self.position[1] - globals.camera_offset_y
        self.rect = self.sprite.get_rect(center=(offset_x, offset_y))
        print(self.rect)
        print(self.sprite)
        
        self.screen.blit(self.sprite, self.rect)

        # for bullet in self.projectiles:
        #     if bullet.is_active and bullet.origin.distance_to(bullet.position) > globals.BULLET_DECAY_DISTANCE:
        #         bullet.reset()
        #     elif bullet.is_active and bullet.position.distance_to(pygame.Vector2(self.player.position[0], self.player.position[1])):
        #         globals.current_player_health -= 1
        #         bullet.reset()
        #     else:
        #         bullet.move()
        #         bullet.draw(self.screen)

    
    def defend(self, player):
        self.player = player
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
            
            # for b in self.projectiles:
            #     if b.is_active == False:
            #         b.shoot_at((self.position[0], self.position[1]), (rx, ry))