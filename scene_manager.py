#-------------------------------------------------------------------------------
# Author:      schmmar1857
# Created:     22.11.2024
#-------------------------------------------------------------------------------

class SceneManager():
    def __init__(self,screen,scene):
        self.screen = screen
        self.scene = scene
    
    def get_current_scene(self):
        return self.scene
    
    def set_scene(self,scene):
        self.scene = scene