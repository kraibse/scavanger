#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     26.11.2024
# Version:     1
#-------------------------------------------------------------------------------

import pygame

class Button:
    def __init__(self,screen,x,y,image_normal,image_hover,text,scale) -> None:
        self.screen = screen
        width = image_normal.get_width()
        height = image_normal.get_height()
        self.image_normal = pygame.transform.scale(image_normal,(int(width*scale),int(height*scale)))
        self.image_hover = pygame.transform.scale(image_hover,(int(width*scale),int(height*scale)))
        self.text = text

        self.button_font = pygame.font.SysFont("freesans",32)
        self.image_current = self.image_normal
        self.rect = self.image_current.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.set_image(self.image_hover)
                self.clicked = True
                print('CLICKED')
        else:
            self.set_image(self.image_normal)
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
        self.screen.blit(self.button_font,(self.rect.x,self.rect.y))
    
    def set_image(self,image):
        self.image_current = image
