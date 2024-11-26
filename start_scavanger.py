import pygame
import asyncio

from scene_manager import SceneManager
from levels import Level1, Level2

SCREEN_W, SCREEN_H = 600,400
FPS = 60

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.loop = asyncio.get_event_loop()

        self.scene_manager = SceneManager(self.screen,'level1')
        self.level1 = Level1(self.screen,self.scene_manager)
        self.level2 = Level2(self.screen,self.scene_manager)
        self.scenes = {'level1': self.level1,'level2':self.level2}
    
    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
            
            self.loop.run_until_complete(self.update())
                    
            self.scenes[self.scene_manager.get_current_scene()].run()
            pygame.display.update()
            self.clock.tick(FPS)

    async def update(self):
        await asyncio.sleep(0)

    def get_delta_time(self):
        return self.clock.tick(60) / 1000


if __name__ == '__main__':
    game = Game()
    game.run()