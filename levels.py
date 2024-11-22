class Scene:
    def __init__(self,screen,scene_manager) -> None:
        self.screen = screen
        self.scene_manager = scene_manager
    
    def run():
        pass

class Level1(Scene):
    def run(self):
        self.screen.fill('red')

class Level2(Scene):
    def run(self):
        self.screen.fill('blue')