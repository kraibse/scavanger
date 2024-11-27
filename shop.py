'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-27

@description: Klassen für den Item-Shop
'''

import pygame

import globals
from button import Button

class Shop:
    def __init__(self,surface) -> None:
        self.surface = surface
        image_health = pygame.image.load(globals.BASE_PATH + 'assets/sprites/health/HeartsFrame1.png').convert_alpha()
        self.shop_button = Button(self.surface,globals.SCREEN_W//2,globals.SCREEN_H-30,text='Shop',action='toggle_shop')

        self.health_button = Button(self.surface,globals.SCREEN_W//2,globals.SCREEN_H//2,image_health,image_health,'',scale=2,action='')
        self.shop_elements = [
            self.health_button
        ]

    def draw(self):
        self.shop_button.draw()
        if self.is_visible():
            for element in self.shop_elements:
                self.health_button.draw()

    def is_visible(self):
        return globals.shop_active
        