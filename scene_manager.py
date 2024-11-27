'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-22

@description: Klassen zum Managen des aktuellen Levels/Scene
'''

from globals import current_scene

class SceneManager():
    def __init__(self,screen):
        self.screen = screen

    @classmethod
    def set_scene(self,scene):
        global current_scene
        current_scene = scene

    @classmethod
    def get_current_scene(self):
        return current_scene