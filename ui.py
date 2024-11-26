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
        image_main_menu = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/main_menu.png').convert_alpha()
        self.shop_button = Button(self.screen,SCREEN_W//2,SCREEN_H-30,image_button_normal,image_button_hover,text='Shop',action='open_shop')
        self.main_menu_button = Button(self.screen,SCREEN_W-30,30,image_main_menu,image_main_menu,scale=1.5,action='main_menu')
        self.level_box = TextBox(self.screen,20,SCREEN_H-50,f'Level: _')
        self.health_box = TextBox(self.screen,20,20,f'Health: _/5')
        self.cash_box = TextBox(self.screen,20,60,f'Cash: _')
        self.info = TextBox(self.screen,SCREEN_W-150,SCREEN_H-30,'Hold space to move...',15)

        self.buttons = [
            self.shop_button,
            self.main_menu_button,
        ]
        self.text_boxes = [
            self.health_box,
            self.cash_box,
            self.level_box,
            self.info,
        ]

    def draw(self):
        for button in self.buttons:
            button.draw()
        for text_box in self.text_boxes:
            text_box.draw()
