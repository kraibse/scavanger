'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-26

@description: Klasse zum Nutzen von diversen TextBoxen
'''

import pygame
import globals

class TextBox:
    def __init__(self,surface,x,y,text,font_size=32,dynamic_text=''):
        self.surface = surface
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont("freesans",font_size)
        self.text_surface = self.font.render(self.text,True,'white')
        self.rect = self.text_surface.get_rect(center=(x,y))
        self.dynamic_text = dynamic_text
    
    def draw(self):
        self.text = self.get_text_value()
        self.text_surface = self.font.render(self.text,True,'white')
        self.surface.blit(self.text_surface,(self.rect.x,self.rect.y))
    
    def get_text_value(self):
        match self.dynamic_text:
            case 'mined_resources':
                return str(globals.mined_resources)
            case 'current_resources':
                return str(globals.current_resouces)
            case 'health_price':
                return str(globals.upgrade_health_price)
            case 'range_price':
                return str(globals.upgrade_range_price)
            case 'current_scene':
                return str(globals.current_scene)
            case _:
                return self.text
            