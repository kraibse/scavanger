'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-27

@description: Klassen für den Item-Shop
'''

import pygame
import os

from globals import BASE_PATH,SCREEN_W,SCREEN_H
import globals
from button import Button
from text_box import TextBox

class Shop:
    def __init__(self,surface) -> None:
        self.surface = surface
        image_health = pygame.image.load(os.path.normpath(BASE_PATH + 'assets/sprites/health/HeartsFrame1.png')).convert_alpha()
        image_health = pygame.transform.scale2x(image_health)
        self.shop_button = Button(self.surface,SCREEN_W//2,SCREEN_H-30,text='Shop',action='toggle_shop')
        self.shop_title = TextBox(self.surface,SCREEN_W//2,SCREEN_H//2,'Shop',50)

        self.health_upgrade = ShopElement(self.surface,SCREEN_W//2,SCREEN_H*0.7,'+1 Health',image_health,'health_price')
        self.speed_upgrade = ShopElement(self.surface,SCREEN_W//2,SCREEN_H*0.8,'x2 Range',image_health,'range_price')

        self.shop_elements = [
            self.health_upgrade,
            self.speed_upgrade,
        ]

    def draw(self):
        self.set_current_prices()
        if self.is_visible():
            self.draw_shop_border()
            self.shop_button.move_to(SCREEN_W//2,SCREEN_H*0.6)
            for element in self.shop_elements:
                element.draw()
        else:
            self.shop_button.move_to(SCREEN_W//2,SCREEN_H-30)
        self.shop_button.draw()
    
    def draw_shop_border(self):
        border_width = 5
        border_color = ((7,32,30))
        rect_width = SCREEN_W*0.5
        rect_height = SCREEN_H*0.4

        pygame.draw.rect(self.surface,border_color,(int(SCREEN_W/2-rect_width/2)-border_width,SCREEN_H*0.6-border_width,rect_width+border_width*2,rect_height+border_width*2))
        pygame.draw.rect(self.surface,'black',(int(SCREEN_W/2-rect_width/2),SCREEN_H*0.6,rect_width,rect_height))

    def is_visible(self):
        return globals.shop_active

    def set_current_prices(self):
        globals.upgrade_health_price = globals.current_player_health*10
        globals.upgrade_range_price = globals.mining_range*1

class ShopElement:
    def __init__(self,surface,x,y,info_text,item_image,dynamic_text) -> None:
        self.surface = surface
        image_resources = pygame.image.load(os.path.normpath(BASE_PATH + 'assets/ore/Ore_Copper_2.png')).convert_alpha()
        image_resources = pygame.transform.scale(image_resources,(30,30))
        self.x = x
        self.y = y
        self.info_text = info_text
        self.item_image = item_image
        self.item_icon = Button(self.surface,self.x-SCREEN_W*0.2,self.y,image_normal=self.item_image,image_hover=self.item_image)
        self.resource_icon = Button(self.surface,self.x-SCREEN_W*0.13,self.y,image_normal=image_resources,image_hover=image_resources)
        self.resource_price_text_box = TextBox(self.surface,self.x-SCREEN_W*0.1,self.y,'0',dynamic_text=dynamic_text,font_size=20)
        self.description_text_box = TextBox(self.surface,self.x,self.y,info_text,font_size=20)
        self.buy_button = Button(self.surface,self.x+SCREEN_W*0.15,self.y,text='Buy',action=f'buy_{dynamic_text}')
    
    def draw(self):
        self.draw_element_border()
        self.item_icon.draw()
        self.resource_icon.draw()
        self.resource_price_text_box.draw()
        self.description_text_box.draw()
        self.buy_button.draw()
    
    def draw_element_border(self):
        border_width = 2
        border_color = 'white'
        rect_width = SCREEN_W * 0.45
        rect_height = SCREEN_H * 0.1

        border_rect = pygame.Rect(0, 0, rect_width + border_width * 2, rect_height + border_width * 2)
        border_rect.center = (self.x, self.y)

        inner_rect = pygame.Rect(0, 0, rect_width, rect_height)
        inner_rect.center = (self.x, self.y)

        pygame.draw.rect(self.surface, border_color, border_rect)
        pygame.draw.rect(self.surface, 'black', inner_rect)