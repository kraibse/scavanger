'''
@author: Leon Horn, Marcus Schmidt
@version: 1.0

@datum: 2024-11-26

@description: Global zugängliche Variablen und Konstanten, die im Spielverlauf angepasst und abgefragt werden
'''

import os

SCREEN_W = 1000
SCREEN_H = 600

MAP_X0 = -SCREEN_W
MAP_Y0 = -SCREEN_H
MAP_X1 = SCREEN_W * 2
MAP_Y1 = SCREEN_H * 2

# Camera
camera_offset_x = 0
camera_offset_y = 0

# planet config
PLANET_TYPES = ["Snow White", "Endor", "Mars", "Earth"]

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'

# player properties
MIN_DISTANCE_TO_CURSOR = 48
MAX_PLAYER_SPEED = 5
mining_range = 32
mining_speed = 0.5
current_player_health = 3

# score 
mined_resources = 0

# level
current_scene = 'MainMenu' #'MainMenu'|'Level 1'|'Level 2'
init_all_scenes = True

# shop
shop_active = False
current_resouces = 0
upgrade_health_price = 50
upgrade_range_price = 50

# Asteroid properties
asteroid_types = ['asteroid-01', 'asteroid-02', 'asteroid-03']
ASTEROID_MIN_SPAWN_DISTANCE = 600
ASTEROID_MAX_SPAWN_DISTANCE = 800
ASTEROID_DECAY_DISTANCE = 1000

# Turret properties
ENEMY_TURRET_RANGE = 250
