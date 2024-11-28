'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-22

@description: Klassen zum Managen des aktuellen Levels/Scene
'''

import globals
class SceneManager():
    def __init__(self,screen):
        self.screen = screen

    @classmethod
    def set_scene(self,scene):
        globals.current_scene = scene
        globals.current_player_health = 3
        globals.init_all_scenes = True

    @classmethod
    def get_current_scene(self):
        return globals.current_scene