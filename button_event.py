'''
@author: Marcus Schmidt
@version: 2.0

@datum: 2024-11-27

@description: Logik für alle Button Events
'''

import globals

def toggle_shop():
    globals.shop_active = not globals.shop_active
    print(globals.shop_active)