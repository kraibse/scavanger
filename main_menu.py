'''
@author: Marcus Schmidt
@version: 1.0

@datum: 2024-11-29

@description: HauptMenu Klasse
'''
import pygame

from levels import Scene
from text_box import TextBox
from button import Button
from globals import SCREEN_W,SCREEN_H, BASE_PATH

class MainMenu(Scene):
    def __init__(self, screen, scene_manager) -> None:
        super().__init__(screen, scene_manager)
        background = pygame.image.load(BASE_PATH + 'assets/background/main_menu.png').convert_alpha()
        self.background = pygame.transform.scale(background,(SCREEN_W,SCREEN_H))
        
        self.title = TextBox(self.screen,SCREEN_W//2,SCREEN_H*0.2,'Scavanger',50)
        self.level1_button = Button(self.screen,SCREEN_W//2,SCREEN_H//2,text='Level 1',action='set_level1')
        self.level2_button = Button(self.screen,SCREEN_W//2,int(SCREEN_H//2+SCREEN_H*0.1),text='Level 2',action='set_level2')

        self.elements = [
            self.title,
            self.level1_button,
            self.level2_button,
        ]
    
    def draw(self):
        super().draw()
        for element in self.elements:
            element.draw()