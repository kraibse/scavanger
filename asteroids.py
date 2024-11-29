'''
@author: Leon Horn
@version: 1.0

@datum: 2024-11-29

@description:
Herumfliegende Asteroiden, die vom Spieler abgebaut werden können und verschwinden, wenn sie weit genug vom Spieler weg sind.
'''
import os
import random
import math
import pygame

from scavengeable import Scavengeable
from shop import Shop

import globals
from globals import BASE_PATH, ASTEROID_MAX_SPAWN_DISTANCE, ASTEROID_MIN_SPAWN_DISTANCE


class Asteroid(Scavengeable):
    def __init__(self, screen, level, maxDurability : int, resourceDrops : int):
        super().__init__(screen, maxDurability, resourceDrops)
        self.level = level
         
        self.randomize_position()
        self.randomize_direction()
        self.randomize_type()
        self.randomize_size()
        self.randomize_movement_speed()
        
    def draw(self):
        scaled_sprite = self.get_scaled_sprite()        
        
        if scaled_sprite is None:
            return
        
        offset_x = self.position[0] - globals.camera_offset_x - self.radius
        offset_y = self.position[1] - globals.camera_offset_y - self.radius
        
        self.screen.blit(scaled_sprite, (offset_x, offset_y))
    
    def is_colliding(self, player):
        player_sprite = player.get_current_animation()._get_current_sprite()
        asteroid_sprite = self.get_current_sprite()

        if player_sprite is None or asteroid_sprite is None:
            return False

        player_rect = player_sprite.get_rect(center=(player.position[0] - globals.camera_offset_x, player.position[1] - globals.camera_offset_y))
        asteroid_rect = asteroid_sprite.get_rect(center=(self.position[0] - globals.camera_offset_x, self.position[1] - globals.camera_offset_y))

        # print(f"Player Rect: {player_rect}, Asteroid Rect: {asteroid_rect}")

        return asteroid_rect.colliderect(player_rect)
    
    def get_current_sprite(self):
        return self.sprite
    
    def get_scaled_sprite(self):
        sprite = self.get_current_sprite()
        
        # Scaling the planet according to the resource drops
        sw = self.size + self.resourceDrops
        self.radius = sw / 2
        self.scaled_sprite = pygame.transform.scale(sprite, (sw, sw))
        
        return self.scaled_sprite
    
    def move(self):
        if self.level.shop.is_visible():
            return
        
        new_x = self.position[0] + self.direction.x * self.movement_speed
        new_y = self.position[1] + self.direction.y * self.movement_speed
        
        # if the asteroid is too far from the player, reset the position and direction
        
        self.position = [new_x, new_y]
    
    def randomize_direction(self):
        base_vector = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.direction = base_vector.normalize()
    
    def randomize_movement_speed(self):
        self.movement_speed = random.uniform(1, 5)
    
    def randomize_position(self):
        base_vector = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        base_vector.rotate(random.uniform(0, 359))
        base_vector.normalize()
        base_vector.scale_to_length(random.uniform(ASTEROID_MIN_SPAWN_DISTANCE, ASTEROID_MAX_SPAWN_DISTANCE))
        
        # Spawn the asteroids around the player
        px = globals.SCREEN_W / 2
        py = globals.SCREEN_H / 1
        
        self.position = [
            px + base_vector.x,
            py + base_vector.y
        ]
    
    def randomize_size(self):
        self.size = random.randint(2, 6)
    
    def randomize_type(self):
        self.asteroid_type = random.choice(['asteroid-01', 'asteroid-02', 'asteroid-03'])
        self.sprite = pygame.image.load(os.path.normpath(BASE_PATH + f'assets/asteroids/{self.asteroid_type}.png'))
