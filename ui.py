#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     26.11.2024
# Version:     2
#-------------------------------------------------------------------------------

import pygame

from globals import SCREEN_W, SCREEN_H, BASE_PATH
from button import Button
from text_box import TextBox

class UI:
    def __init__(self,screen) -> None:
        self.screen = screen
        image_button_normal = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Button Normal.png').convert_alpha()
        image_button_hover = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Button Hover.png').convert_alpha()
        self.shop_button = Button(self.screen,100,100,image_button_normal,image_button_hover,'Shop',1)
        self.cash_button = Button(self.screen,300,100,image_button_normal,image_button_hover,'Test',1)
        self.level_button = Button(self.screen,500,100,image_button_normal,image_button_hover,'Test2',0.5)
        self.text_box1 = TextBox(self.screen,500,500,'minerals')

        self.buttons = [
            self.level_button,
            self.shop_button,
            self.cash_button,
        ]
        self.text_boxes = [
            self.text_box1
        ]

    def draw(self):
        for button in self.buttons:
            button.draw()
        for text_box in self.text_boxes:
            text_box.draw()
