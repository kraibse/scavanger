'''
@author: Marcus Schmidt
@version: 1.0

@datum: 2024-11-27

@description: Logik für alle Button Events
'''

from globals import *

def toggle_shop():
    global shop_active
    shop_active = not shop_active
    print(shop_active)