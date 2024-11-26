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
        image_shop_button_normal = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Button Normal.png').convert_alpha()
        image_shop_button_hover = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Button Normal.png').convert_alpha()
        self.shop_button = Button(self.screen,100,100,image_shop_button_normal,image_shop_button_hover,'Shop',1)
        self.cash_button = Button(self.screen,100,100,image_shop_button_normal,image_shop_button_hover,'Shop',1)
        self.shop_button = Button(self.screen,100,100,image_shop_button_normal,image_shop_button_hover,'Shop',1)


    def draw(self):
        self.play_button.draw()
