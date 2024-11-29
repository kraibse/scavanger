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
from shop import Shop

import globals
from globals import SCREEN_W, SCREEN_H, MIN_DISTANCE_TO_CURSOR, MAX_PLAYER_SPEED


class Player():
    def __init__(self, level):
        w = SCREEN_W
        h = SCREEN_H
        
        self.level = level
        
        self.position = [math.floor(w / 2), math.floor(h / 2)]
        base_path = os.path.dirname(os.path.abspath(__file__)) + '/assets/sprites/player/'
        
        self.animations = {
            "idle": SpriteAnimation(base_path, 'player0', 1)
        }

        self.current_animation = "idle"
        
        self.clock = pygame.time.Clock()
        self.dt = 0
        
        self.size = self.get_current_animation()._get_current_sprite().get_width()

    def change_animation(self, new_anim="idle"):
        animation = self.get_current_animation()
        asyncio.run(animation.stop())
        
        self.current_animation = new_anim
        asyncio.run(animation.play())
    
    def damage(self):
        globals.current_player_health -= 1
    
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
        
        # draw mining range
        self.mining_area = pygame.draw.circle(self.level.screen, pygame.Color(255, 220, 0, a=100), self.get_center_rect().center, globals.mining_range, width=2)        
        
        # draw planet radar
        self.draw_planet_radar()
        
        self.level.screen.blit(rotated_sprite, sprite_rect)

    def draw_planet_radar(self):
        for planet in self.level.planets:
            if planet is None:
                continue
            
            # planet_rect = planet.get_current_sprite().get_rect().center
            planetx = planet.position[0] - globals.camera_offset_x
            planety = planet.position[1] - globals.camera_offset_y
            distance = self.get_player_distance_to(planetx, planety)
            
            player_position = pygame.math.Vector2(self.position[0], self.position[1])
            blip_position = player_position.move_towards(pygame.math.Vector2(planetx, planety), globals.mining_range)
            
            pygame.draw.circle(self.level.screen, pygame.Color(255, 220, 0, a=100), blip_position, 5)

    def get_current_animation(self):
        return self.animations.get(self.current_animation)

    def get_size(self):
        return self.size

    def is_accelerating(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        
        return False
    
    def is_colliding(self, planet):
        if planet is None:
            return False
        
        planetx = planet.position[0] - globals.camera_offset_x
        planety = planet.position[1] - globals.camera_offset_y
        distance = self.get_player_distance_to(planetx, planety)
        
        if distance > globals.mining_range + planet.radius:
            return False
        
        # print(f"Distance to planet: {distance}, mining range: {globals.MINING_RANGE}, planet radius: {planet.radius}")
        return True

    def get_center_rect(self):
        center_rect = self.get_current_animation()._get_current_sprite().get_rect(center=(self.position[0], self.position[1]))
        return center_rect
    
    def get_player_distance_to(self, tx, ty):
        mx = tx - self.position[0]
        my = ty - self.position[1]

        distance = math.sqrt(mx ** 2 + my ** 2)
        return distance

    def move(self):
        if self.level.shop.is_visible():
            return
        
        self.current_animation = "idle"

        mousex, mousey = pygame.mouse.get_pos()
        distance = self.get_player_distance_to(mousex, mousey)
        if distance <= MIN_DISTANCE_TO_CURSOR:
            return

        mx = mousex - self.position[0]
        my = mousey - self.position[1]
        motion = [mx / distance * MAX_PLAYER_SPEED, my / distance * MAX_PLAYER_SPEED]    # move the player at a constant speed for now

        if self.is_accelerating():
            # self.position[0] += motion[0]
            # self.position[1] += motion[1]
            globals.camera_offset_x += motion[0]
            globals.camera_offset_y += motion[1]
            
            # print(globals.camera_offset_x, globals.camera_offset_y)


    def mine(self, planet):
        remaining_resources = planet.get_remaining_resources()
        if remaining_resources <= 0:
            self.level.destroy_planet(planet)
            return

        if self.dt > globals.mining_speed:
            globals.mined_resources += 1
            globals.current_resouces += 1
            planet.set_remaining_resources(remaining_resources - 1)
            self.dt = 0
        else:
            self.dt += self.clock.tick(60)