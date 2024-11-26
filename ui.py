#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     26.11.2024
#-------------------------------------------------------------------------------

import pygame

from globals import SCREEN_W, SCREEN_H, BASE_PATH
from button import Button

class UI:
    def __init__(self,screen) -> None:
        self.screen = screen
        image_play_button = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/placeholder.png').convert_alpha()
        self.play_button = Button(self.screen,100,100,image_play_button,1)

    def draw(self):
        self.play_button.draw()
