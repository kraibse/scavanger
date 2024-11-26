from player import Player


class Scene:
    w = 720
    h = 480
    
    def __init__(self,screen,scene_manager) -> None:
        self.screen = screen
        self.scene_manager = scene_manager
        self.player = Player(self)

        self.enemies = self.spawn_enemies()
        self.planet = self.spawn_planets()
    
    def run(self):
        pass

    def draw(self):
        self.player.draw()

        for enemy in self.enemies:
            enemy.draw()

        for planet in self.planets:
            planet.draw()

    def spawn_enemies(self):
        return []
    
    def spawn_planets(self):
        return []


class Level1(Scene):
    def run(self):
        self.screen.fill('red')

class Level2(Scene):
    def run(self):
        self.screen.fill('blue')