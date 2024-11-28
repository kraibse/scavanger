'''
@author: Marcus Schmidt
@version: 3.0

@datum: 2024-11-26

@description: Klasse für die Darstellung des LevelUI's
'''
import os
import pygame

from globals import SCREEN_W, SCREEN_H, BASE_PATH
from button import Button
from text_box import TextBox
from health_bar import HealthBar

class UI:
    def __init__(self,screen) -> None:
        self.screen = screen
        image_main_menu = pygame.image.load(os.path.normpath(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/main_menu.png')).convert_alpha()
        image_resources = pygame.image.load(os.path.normpath(BASE_PATH + 'assets/ore/Ore_Copper_2.png')).convert_alpha()

        self.main_menu_button = Button(self.screen,SCREEN_W-30,SCREEN_H*0.05,image_main_menu,image_main_menu,scale=1.5,action='main_menu')
        self.resource_button = Button(self.screen,SCREEN_W*0.04,SCREEN_H*0.133,image_resources,image_resources,scale=0.08)
        self.resource_box = TextBox(self.screen,SCREEN_W*0.07,SCREEN_H*0.133,'',dynamic_text='current_resources')
        self.level_box = TextBox(self.screen,SCREEN_W*0.02,SCREEN_H-SCREEN_H*0.05,'',dynamic_text='level')
        self.info = TextBox(self.screen,SCREEN_W-SCREEN_W*0.11,SCREEN_H-SCREEN_H*0.033,'Hold space to move...',15)

        self.health_bar = HealthBar(self.screen,SCREEN_W*0.02,SCREEN_H*0.033)
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