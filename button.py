import pygame

class Button:
    def __init__(self,screen,x,y,image,scale) -> None:
        self.screen = screen
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                print('CLICKED')
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
        self.screen.blit(self.image,(self.rect.x,self.rect.y))
