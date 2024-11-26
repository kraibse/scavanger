import os

SCREEN_W = 1000
SCREEN_H = 600

MAP_X0 = -SCREEN_W
MAP_Y0 = -SCREEN_H
MAP_X1 = SCREEN_W * 2
MAP_Y1 = SCREEN_H * 2

BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'


# player properties
MIN_DISTANCE_TO_CURSOR = 48
MAX_PLAYER_SPEED = 5