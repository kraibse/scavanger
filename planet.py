from scavengeable import Scavengeable
from globals import BASE_PATH
from animated_sprite import SpriteAnimation

class Planet(Scavengeable):
    def __init__(self, screen, maxDurability, resourceDrops):
        super(screen, maxDurability, resourceDrops)
        
        self.screen = screen
        self.position = [0, 0]
        
        self.animation = SpriteAnimation(BASE_PATH, 'Lava', 1, '.png')
        
    def draw(self):
        current_sprite = self.get_current_sprite()
        
        if current_sprite is None:
            return
        
        self.screen.blit(current_sprite, (self.position[0], self.position[1]))
        
    def get_current_sprite(self):
        self.animation._get_current_sprite()
        
    def set_type(self, planet_type):
        sprite_path = BASE_PATH + 'assets/planets/' + planet_type + '.png'