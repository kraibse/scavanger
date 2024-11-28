'''
@author: Lucian Kath
@version: 1.0

@datum: 2024-11-22

@description: Basisklasse der abbaubaren Spielelemente 
'''
import math
import pygame

class Scavengeable:
    def __init__(self, screen, maxDurability : int, resourceDrops : int):
        self.screen = screen
        self.resourceDrops = resourceDrops
        self.maxDurability = maxDurability
        self.durability = maxDurability
        
    def draw(self):
        scaled_sprite = self.get_scaled_sprite()        
        
        if scaled_sprite is None:
            return
        
        offset_x = self.position[0] - globals.camera_offset_x - self.radius
        offset_y = self.position[1] - globals.camera_offset_y - self.radius
        
        self.screen.blit(scaled_sprite, (offset_x, offset_y))

    def get_scaled_sprite(self):
        sprite = self.get_current_sprite()
        
        # Scaling the planet according to the resource drops
        sx = sprite.get_width() + 5 * self.resourceDrops
        sy = sprite.get_height() + 5 * self.resourceDrops
        
        self.radius = math.floor(sx / 2)
        self.scaled_sprite = pygame.transform.scale(sprite, (sx, sy))
        
        return self.scaled_sprite

    def scavenge(self, damage) -> int:
        self.durability = max(0, self.durability - damage)
        if self.durability <= 0 and self.isFullyScavenged:
            self.onFullyScavenged()
        return self.resourceDrops * (damage / self.maxDurability)
    
    def onFullyScavenged(self):
        self.isFullyScavenged = True
        pass