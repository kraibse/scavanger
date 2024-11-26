#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     26.11.2024
# Version:     2
#-------------------------------------------------------------------------------

import pygame

class TextBox:
    def __init__(self,surface,x,y,text,font_size=32):
        self.surface = surface
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.SysFont("freesans",font_size)
        self.text_surface = self.font.render(self.text,True,'white')
        self.rect = self.text_surface.get_rect(topleft=(x,y))
    
    def draw(self):
        self.surface.blit(self.text_surface,(self.rect.x,self.rect.y))