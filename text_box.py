#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     26.11.2024
# Version:     1
#-------------------------------------------------------------------------------

import pygame

class TextBox:
    def __init__(self,surface,x,y,text):
        self.surface = surface
        self.x = x
        self.y = y
        self.text = text

        self.font = pygame.font.SysFont("freesans",32)
    
    def draw(self):
        pass