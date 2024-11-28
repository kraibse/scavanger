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

def buy_health():
    if globals.current_resouces >= globals.upgrade_health_price:
        globals.current_player_health += 1
        globals.current_resouces -= globals.upgrade_health_price

def buy_range():
    if globals.current_resouces >= globals.upgrade_range_price:
        globals.mining_range *= 2
        globals.current_resouces -= globals.upgrade_range_price
