#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     22.11.2024
# Version:     3
#-------------------------------------------------------------------------------

import pygame
import os
import random

from player import Player
from planet import Planet
from ui import UI

from globals import *

class Scene:
    PATH_PLACEHOLDER_BACKGROUND = BASE_PATH + 'assets/background/placeholder_background.png'
    PATH_PLACEHOLDER_BACKGROUND2 = BASE_PATH + 'assets/background/placeholder_background2.png'
    PATH_BACKGROUND_LEVEL1 = BASE_PATH + 'assets/background/purple_nebula_background.png'
    PATH_BACKGROUND_LEVEL2 = BASE_PATH + 'assets/background/Green_Nebula_07-1024x1024.png'
    IMAGE_PLAY_BUTTON = BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Default.png'

    def __init__(self,screen,scene_manager, total_planets) -> None:
        self.screen = screen
        self.scene_manager = scene_manager
        self.total_planets = total_planets
        self.background = pygame.image.load(Scene.PATH_PLACEHOLDER_BACKGROUND).convert_alpha()
        self.widht = self.background.get_width()
        self.height = self.background.get_height()
        self.enemies = self.spawn_enemies()
        
        self.spawn_planets()
        
        self.ui = UI(self.screen)
        self.player = Player(self)
    
    def run(self):
        self.draw()
        
    def destroy_planet(self, planet):
        self.planets.remove(planet)

    def draw(self):
        self.screen.blit(self.background,(0,0))

        for planet in self.planets:
            if self.player.is_colliding(planet):
                print("Player is colliding with the planet")
            planet.draw()

        for enemy in self.enemies:
            enemy.draw()

        self.player.move()
        self.player.draw()
        
        self.ui.draw()
        
    def spawn_enemies(self):
        return []
    
    def spawn_planets(self):
        self.planets = []
        
        for planet in range(self.total_planets):
            rx = random.randint(MAP_X0, MAP_X1)
            ry = random.randint(MAP_Y0, MAP_Y1)
            
            new_planet = Planet(self.screen, 100, random.randint(3, 20))
            new_planet.set_type(random.choice(["Lava", "Baren"]))
            new_planet.set_position(rx, ry)
            self.planets.append(new_planet)
        
        return self.planets


class Level1(Scene):
    def __init__(self, screen, scene_manager) -> None:
        total_planets = 5
        
        super().__init__(screen, scene_manager, total_planets)
        self.background = pygame.image.load(Scene.PATH_BACKGROUND_LEVEL1).convert_alpha()
    
    def spawn_enemies(self):
        return []


class Level2(Scene):
    def __init__(self, screen, scene_manager) -> None:
        total_planets = 10
        
        super().__init__(screen, scene_manager, total_planets)
        self.background = pygame.image.load(Scene.PATH_BACKGROUND_LEVEL2).convert_alpha()
    
    def spawn_enemies(self):
        return []
    