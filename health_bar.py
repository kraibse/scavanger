'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-29

@description: Klasse für die Lebensleiste 
'''

import pygame

import globals

class HealthBar:
    def __init__(self,surface,x,y) -> None:
        image_heart = pygame.image.load(globals.BASE_PATH + 'assets\sprites\health\HeartsFrame1.png').convert_alpha()
        self.image_heart_full = pygame.transform.scale2x(image_heart)
        self.image_width = self.image_heart_full.get_width()
        self.surface = surface
        self.x = x
        self.y = y
        self.current_hp = self.get_health()

    def draw(self):
        self.current_hp = self.get_health()
        for i in range(self.current_hp):
            x_pos = int(self.x + self.image_width/1.5 * i) #Herzen sollen leicht überlappen
            self.surface.blit(self.image_heart_full, (x_pos, self.y)) 
    
    def get_health(self):
        return globals.current_player_health