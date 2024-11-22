import pygame

SCREEN_W, SCREEN_H = 600,400
FPS = 60
running = True

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
        self.clock = pygame.time.Clock()
    
    def run(self):
        global running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        self.clock.tick(FPS)


if __name__ == '__name__':
    game = Game()
    game.run()