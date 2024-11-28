'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-26

@description: Klasse zum Nutzen von diversen Buttons
'''

import os
import pygame
import button_event
from globals import BASE_PATH

class Button:
    def __init__(self,screen,x,y,image_normal=None,image_hover=None,text='',scale=1,action='') -> None:
        self.screen = screen
        if not image_normal:
            image_normal = pygame.image.load(os.path.normpath(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Button Normal.png')).convert_alpha()
        if not image_hover:
            image_hover = pygame.image.load(os.path.normpath(BASE_PATH + 'assets/buttons/Rect-Medium/PlayIcon/Button Hover.png')).convert_alpha()
        width = image_normal.get_width()
        height = image_normal.get_height()
        self.image_normal = pygame.transform.scale(image_normal,(int(width*scale),int(height*scale)))
        self.image_hover = pygame.transform.scale(image_hover,(int(width*scale),int(height*scale)))
        self.text = text
        self.action = action

        self.image_current = self.image_normal
        self.rect = self.image_current.get_rect()
        self.rect.center = (x,y)
        self.clicked = False

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.set_image(self.image_hover)
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.button_action()
        else:
            self.set_image(self.image_normal)

        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        self.screen.blit(self.image_current, (self.rect.x, self.rect.y))
        self.draw_text()

    def draw_text(self):
        if self.text == '':
            return
        max_width, max_height = self.rect.width, self.rect.height
        font_size = 32
        font = pygame.font.SysFont("freesans", font_size)
        text_surface = font.render(self.text, True, 'white')

        while text_surface.get_width() > max_width or text_surface.get_height() > max_height:
            font_size -= 1
            font = pygame.font.SysFont("freesans", font_size)
            text_surface = font.render(self.text, True, 'white')

        text_x = self.rect.x + (self.rect.width - text_surface.get_width()) // 2
        text_y = self.rect.y + (self.rect.height - text_surface.get_height()) // 2
        self.screen.blit(text_surface, (text_x, text_y))

    def set_image(self, image):
        self.image_current = image
    
    def move_to(self,x,y):
        self.rect.center = (x,y)
    
    def button_action(self):
        match self.action:
            case 'toggle_shop':
                button_event.toggle_shop()
            case 'set_level1':
                button_event.set_scene('Level 1')
            case 'set_level2':
                button_event.set_scene('Level 2')
            case _:
                print('no method') #TODO delete after test