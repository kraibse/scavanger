'''
@author: Marcus Schmidt
@version: 3.0

@datum: 2024-11-26

@description: Klasse für die Darstellung des LevelUI's
'''

import pygame

from globals import SCREEN_W, SCREEN_H, BASE_PATH
from button import Button
from text_box import TextBox
from health_bar import HealthBar

class UI:
    def __init__(self,screen) -> None:
        self.screen = screen
        image_main_menu = pygame.image.load(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/main_menu.png').convert_alpha()
        image_resources = pygame.image.load(BASE_PATH + 'assets/ore/Ore_Copper_2.png').convert_alpha()

        self.main_menu_button = Button(self.screen,SCREEN_W-30,30,image_main_menu,image_main_menu,scale=1.5,action='main_menu')
        self.resource_button = Button(self.screen,40,80,image_resources,image_resources,scale=0.08)
        self.resource_box = TextBox(self.screen,70,65,'',dynamic_text='mined_resources')
        self.level_box = TextBox(self.screen,20,SCREEN_H-50,'',dynamic_text='level')
        self.info = TextBox(self.screen,SCREEN_W-150,SCREEN_H-30,'Hold space to move...',15)

        self.health_bar = HealthBar(self.screen,20,20)
        self.buttons = [
            self.main_menu_button,
            self.resource_button,
        ]
        self.text_boxes = [
            self.resource_box,
            self.level_box,
            self.info,
        ]

    def draw(self):
        for button in self.buttons:
            button.draw()
        for text_box in self.text_boxes:
            text_box.draw()
        self.health_bar.draw()