import pygame

from globals import BASE_PATH
from scavengeable import Scavengeable
from animated_sprite import SpriteAnimation

class Planet(Scavengeable):
    def __init__(self, screen, maxDurability, resourceDrops):
        super().__init__(screen, maxDurability, resourceDrops)
        
        self.screen = screen
        self.position = [0, 0]
        
        # self.animation = SpriteAnimation(BASE_PATH, 'Lava', 1, '.png')
        
    def draw(self):
        current_sprite = self.get_current_sprite()
        
        if current_sprite is None:
            return
        
        # Scaling the planet according to the resource drops
        sx = current_sprite.get_width() + 5 * self.resourceDrops
        sy = current_sprite.get_height() + 5 * self.resourceDrops
        scaled_sprite = pygame.transform.scale(current_sprite, (sx, sy))
        
        self.screen.blit(scaled_sprite, (self.position[0], self.position[1]))
        
    def get_current_sprite(self):
        # self.animation._get_current_sprite()
        return self.current_sprite
        
    def set_position(self, x, y):
        self.position = [x, y]
        
    def set_type(self, planet_type):
        sprite_path = BASE_PATH + 'assets/planets/' + planet_type + '.png'
        self.current_sprite = pygame.image.load(sprite_path).convert_alpha()