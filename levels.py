import pygame

from player import Player
from ui import UI

class Scene:
    PATH_PLACEHOLDER_BACKGROUND = 'assets/background/placeholder_background.png'
    PATH_PLACEHOLDER_BACKGROUND2 = 'assets/background/placeholder_background2.png'
    IMAGE_PLAY_BUTTON = 'assets/buttons/Rect-Medium/PlayIcon/Default.png'

    def __init__(self,screen,scene_manager) -> None:
        self.screen = screen
        self.scene_manager = scene_manager
        self.background = pygame.image.load(Scene.PATH_PLACEHOLDER_BACKGROUND).convert_alpha()
        self.widht = self.background.get_width()
        self.height = self.background.get_height()
        self.enemies = self.spawn_enemies()
        self.planets = self.spawn_planets()
        self.ui = UI(self.screen)
        # self.player = Player(self) #TODO Player einbauen
    
    def run(self):
        self.draw()

    def draw(self):
        self.screen.blit(self.background,(0,0))
        # self.player.draw()

        for enemy in self.enemies:
            enemy.draw()

        for planet in self.planets:
            planet.draw()
        
        self.ui.draw()
        
    def spawn_enemies(self):
        return []
    
    def spawn_planets(self):
        return []


class Level1(Scene):
    def __init__(self, screen, scene_manager) -> None:
        super().__init__(screen, scene_manager)
        self.background = pygame.image.load(Scene.PATH_PLACEHOLDER_BACKGROUND).convert_alpha()
    
    def spawn_enemies(self):
        return []
    
    def spawn_planets(self):
        return []

class Level2(Scene):
    def __init__(self, screen, scene_manager) -> None:
        super().__init__(screen, scene_manager)
        self.background = pygame.image.load(Scene.PATH_PLACEHOLDER_BACKGROUND2).convert_alpha()
    
    def spawn_enemies(self):
        return []
    
    def spawn_planets(self):
        return []
    