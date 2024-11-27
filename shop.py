#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     27.11.2024
# Version:     1
#-------------------------------------------------------------------------------

import pygame

from button import Button
from globals import *

class Shop:
    def __init__(self,surface) -> None:
        self.surface = surface
        image_health = pygame.image.load(BASE_PATH + 'assets/sprites/health/Half_a_heart2.png').convert_alpha()
        self.health_button = Button(self.surface,SCREEN_W//2,SCREEN_H//2,image_health,image_health,'',scale=2,action='')

        self.elements = [
            self.health_button
        ]

    def draw(self):
        self.health_button.draw()
        