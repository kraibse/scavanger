'''
@author: Marcus Schmidt
@version: 1.0

@datum: 2024-11-22

@description: Haupt-Datei zum Starten des Spiels
'''

import pygame
import asyncio

from scene_manager import SceneManager
from levels import Level1, Level2

class Game:
    SCREEN_W, SCREEN_H = 1000,600
    FPS = 60
    
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Scavanger')
        self.screen = pygame.display.set_mode((Game.SCREEN_W,Game.SCREEN_H))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.scene_manager = SceneManager(self.screen)
        self.level1 = Level1(self.screen,self.scene_manager)
        self.level2 = Level2(self.screen,self.scene_manager)
        self.scenes = {'Level 1': self.level1,'Level 2':self.level2}
    
    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            self.scenes[self.scene_manager.get_current_scene()].run()
            pygame.display.update()
            self.clock.tick(Game.FPS)

    async def update(self):
        await asyncio.sleep(0)

    def get_delta_time(self):
        return self.clock.tick(60) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()