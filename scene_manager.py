'''
@author: Marcus Schmidt
@version: 1.0

@datum: 2024-11-22

@description: Klassen zum Managen des aktuellen Levels/Scene
'''

class SceneManager():
    def __init__(self,screen,scene):
        self.screen = screen
        self.scene = scene
    
    def get_current_scene(self):
        return self.scene
    
    def set_scene(self,scene):
        self.scene = scene