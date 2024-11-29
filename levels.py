'''
@author: Marcus Schmidt
@version: 4.0

@datum: 2024-11-22

@description: Klassen für die jeweiligen Levels
'''

import pygame
import os
import random

from player import Player
from planet import Planet
from enemy_turret import EnemyTurret
from asteroids import Asteroid
from ui import UI
from shop import Shop
from button_event import set_scene

import globals
from globals import *

class Scene:
    PATH_PLACEHOLDER_BACKGROUND = os.path.normpath(BASE_PATH + 'assets/background/placeholder_background.png')
    PATH_PLACEHOLDER_BACKGROUND2 = os.path.normpath(BASE_PATH + 'assets/background/placeholder_background2.png')
    PATH_BACKGROUND_LEVEL1 = os.path.normpath(BASE_PATH + 'assets/background/purple_nebula_background.png')
    PATH_BACKGROUND_LEVEL2 = os.path.normpath(BASE_PATH + 'assets/background/Green_Nebula_07-1024x1024.png')
    IMAGE_PLAY_BUTTON = os.path.normpath(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Default.png')

    def __init__(self,screen,scene_manager) -> None:
        self.screen = screen
        self.scene_manager = scene_manager
        background = pygame.image.load(Scene.PATH_PLACEHOLDER_BACKGROUND).convert_alpha()
        self.background = pygame.transform.scale(background,(SCREEN_W,SCREEN_H))
        self.widht = self.background.get_width()
        self.height = self.background.get_height()
        self.shop = Shop(self.screen)     
        self.ui = UI(self.screen)
    
    def run(self):
        self.draw()
        
    def destroy_planet(self, planet):
        self.planets.remove(planet)

    def draw(self):
        self.screen.blit(self.background,(0,0))


class Level(Scene):
    def __init__(self, screen, scene_manager, total_planets, total_asteroids, total_enemies) -> None:
        super().__init__(screen, scene_manager)
        self.total_planets = total_planets
        self.total_asteroids = total_asteroids
        self.total_enemies = total_enemies
        self.spawn_enemies()
        self.spawn_planets()
        self.spawn_asteroids()
        self.player = Player(self)
        self.transition_counter_current = 0
        self.transition_counter_max = SCREEN_W//2
        self.next_scene = 'GameWon'
    
    def draw(self):
        if self.transition_counter_current <= self.transition_counter_max:
            self.level_transition()
            return
        if not self.planets:
            self.set_next_scene()
        if globals.current_player_health <= 0:
            self.next_scene = 'GameOver'
            self.set_next_scene()

        super().draw()
        
        for planet in self.planets:
            if self.player.is_colliding(planet):
                self.player.mine(planet)
                
            planet.draw()
            
        for asteroid in self.asteroids:
            # if asteroid is too far from the player, reset position and direction
            ax = asteroid.position[0] - globals.camera_offset_x
            ay = asteroid.position[1] - globals.camera_offset_y
            asteroid_position = pygame.Vector2(ax, ay)
            
            player_position = pygame.Vector2(self.player.position[0], self.player.position[1])
            
            distance = asteroid_position.distance_to(player_position)
            
            is_asteroid_colliding = False
            if distance < self.player.get_size() + asteroid.size:
                is_asteroid_colliding = True # asteroid.is_colliding(self.player)
    
            if is_asteroid_colliding:
                self.player.damage()

            if is_asteroid_colliding or distance > ASTEROID_DECAY_DISTANCE:
                asteroid.randomize_position()
                asteroid.randomize_direction()

            asteroid.move()
            asteroid.draw()

        for enemy in self.enemies:
            enemy.draw()
            enemy.defend(self.player)

        if (globals.current_player_health > 0):
            self.player.move()
            self.player.draw()
        
        self.ui.draw()
        self.shop.draw()
        
    def spawn_asteroids(self):
        self.asteroids = []
        
        for a in range(self.total_asteroids):
            asteroid = Asteroid(self.screen, self, 100, random.randint(30, 200))
            self.asteroids.append(asteroid)
        
    def spawn_enemies(self):
        self.enemies = []

        for e in range(self.total_enemies):
            enemy = EnemyTurret(self.screen, 100, random.randint(30, 200))
            self.enemies.append(enemy)
        
        return self.enemies
    
    def spawn_planets(self):
        self.planets = []
        
        for planet in range(self.total_planets):
            rx = random.randint(MAP_X0, MAP_X1)
            ry = random.randint(MAP_Y0, MAP_Y1)
            
            new_planet = Planet(self.screen, 100, random.randint(3, 20))
            new_planet.set_type(random.choice(PLANET_TYPES))
            new_planet.set_position(rx, ry)
            self.planets.append(new_planet)
        
        return self.planets

    def level_transition(self):
        self.transition_counter_current += SCREEN_W*0.03
        pygame.draw.circle(self.screen,'black',(SCREEN_W//2,SCREEN_H//2),self.transition_counter_current*2)

    def set_next_scene(self):
        if self.next_scene in ['GameWon','GameOver']:
            self.reset_globals()
        set_scene(self.next_scene)
    
    def reset_globals(self):
        globals.current_player_health = 3
        globals.mining_range = 32

class Level1(Level):
    def __init__(self, screen, scene_manager) -> None:
        self.total_planets = 5
        self.total_asteroids = 25
        self.total_enemies = 5
        super().__init__(screen, scene_manager, self.total_planets,self.total_asteroids, self.total_enemies)
        self.next_scene = 'Level 2'
        self.background = pygame.image.load(Scene.PATH_BACKGROUND_LEVEL1).convert_alpha()



class Level2(Level):
    def __init__(self, screen, scene_manager) -> None:
        self.total_planets = 10
        self.total_asteroids = 50
        self.total_enemies = 5
        super().__init__(screen, scene_manager, self.total_planets,self.total_asteroids, self.total_enemies)
        self.next_scene = 'GameWon'
        self.background = pygame.image.load(Scene.PATH_BACKGROUND_LEVEL2).convert_alpha()