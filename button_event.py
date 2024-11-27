'''
@author: Marcus Schmidt
@version: 3.0

@datum: 2024-11-27

@description: Logik für alle Button Events
'''

import globals
from scene_manager import SceneManager

def toggle_shop():
    globals.shop_active = not globals.shop_active
    print(globals.shop_active)

def set_scene(scene):
    SceneManager.set_scene(scene)