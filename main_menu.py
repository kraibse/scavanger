'''
@author: Marcus Schmidt
@version: 1.0

@datum: 2024-11-29

@description: HauptMenu Klasse
'''

from levels import Scene
from button import Button
from globals import SCREEN_W,SCREEN_H

class MainMenu(Scene):
    def __init__(self, screen, scene_manager) -> None:
        super().__init__(screen, scene_manager)
        self.level1_button = Button(self.screen,SCREEN_W//2,SCREEN_H//2,text='Level 1',action='set_level1')
        self.level2_button = Button(self.screen,SCREEN_W//2,int(SCREEN_H//2+SCREEN_H*0.1),text='Level 2',action='set_level2')

        self.elements = [
            self.level1_button,
            self.level2_button,
        ]
    
    def draw(self):
        super().draw()
        for element in self.elements:
            element.draw()